from rest_framework import serializers

from common.constants import Currency
from finances.models import Operation, Category


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.UUIDField(source="user_id", read_only=True)
    type = serializers.IntegerField(default=Currency.RUB)
    parent = serializers.SerializerMethodField()
    title = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = (
            "id",
            "user",
            "type",
            "parent",
            "title",
            "slug",
        )

    def get_parent(self, obj):
        if obj.parent:
            return self.__class__(obj.parent).data
        return None


class OperationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.UUIDField(source="user_id", read_only=True)
    type = serializers.IntegerField(default=Currency.RUB)
    comment = serializers.CharField()
    money = serializers.FloatField()
    currency = serializers.IntegerField()
    category = CategorySerializer()
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
