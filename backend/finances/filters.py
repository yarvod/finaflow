import django_filters.rest_framework as filters

from finances.models import Category


class CategoryFilterSet(filters.FilterSet):
    type = filters.NumberFilter(field_name='type', label='Тип')

    class Meta:
        model = Category
        fields = ["type"]
