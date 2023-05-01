from django.db.models import Q
from rest_framework import serializers

from common.constants import Currency, OperationType
from finances.models import Operation, Category


class CategorySmallGetSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    label = serializers.CharField(source="title")
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "label", "children")

    def get_children(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        if obj.children:
            children = obj.children.filter(Q(user__isnull=True) | Q(user=user))
            return self.__class__(children, many=True).data
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data["children"]:
            data.pop("children")
        return data


class CategoryGetSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.UUIDField(source="user_id", read_only=True)
    type = serializers.IntegerField(default=Currency.RUB)
    parent = serializers.SerializerMethodField()
    title = serializers.CharField()

    class Meta:
        model = Category
        fields = (
            "id",
            "user",
            "type",
            "parent",
            "title",
        )

    def get_parent(self, obj):
        if obj.parent:
            return self.__class__(obj.parent).data
        return None


class CategoryWriteSerializer(serializers.ModelSerializer):
    type = (serializers.IntegerField(),)
    title = (serializers.CharField(),)
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), allow_null=True
    )

    class Meta:
        model = Category
        fields = (
            "type",
            "title",
            "parent",
        )


class OperationListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.UUIDField(source="user_id", read_only=True)
    type = serializers.IntegerField()
    comment = serializers.CharField()
    money = serializers.FloatField()
    currency = serializers.IntegerField()
    category = CategoryGetSerializer()
    date = serializers.DateField()
    categories_titles = serializers.SerializerMethodField()

    class Meta:
        model = Operation
        fields = (
            "id",
            "user",
            "type",
            "comment",
            "money",
            "currency",
            "category",
            "date",
            "categories_titles",
        )

    def get_categories_titles(self, obj):
        if obj.category:
            return obj.category.get_categories_chain_titles()
        return None


class OperationWriteSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField(default=OperationType.EXPENDITURE, required=False)
    comment = serializers.CharField(default="", allow_null=True, allow_blank=True)
    money = serializers.FloatField(default=0)
    currency = serializers.IntegerField(default=Currency.RUB, required=False)
    category = serializers.SlugRelatedField(
        slug_field="id", queryset=Category.objects.all(), allow_null=True
    )
    date = serializers.DateField()

    class Meta:
        model = Operation
        fields = (
            "type",
            "comment",
            "money",
            "currency",
            "category",
            "date",
        )
