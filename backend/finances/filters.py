import django_filters.rest_framework as filters

from finances.models import Category, Operation


class CategoryFilterSet(filters.FilterSet):
    type = filters.NumberFilter(field_name="type", label="Тип")

    class Meta:
        model = Category
        fields = ["type"]


class OperationsFilterSet(filters.FilterSet):
    date = filters.DateFromToRangeFilter(field_name="date", label="Дата")

    class Meta:
        model = Operation
        fields = ["date"]
