from rest_framework import serializers

from finances.models import Operation, Category, SourceOfIncome


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SourceOfIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceOfIncome
        fields = "__all__"


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"
