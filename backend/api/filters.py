from django_filters import Filter
from django_filters.constants import EMPTY_VALUES


class ListFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value_list = value.split(",")
        lookup = "%s__%s" % (self.field_name, self.lookup_expr)
        return qs.filter(**{lookup: value_list}).distinct()
