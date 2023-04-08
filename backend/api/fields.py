from rest_framework import serializers


class TagWritableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        qs = self.get_queryset()
        params = {self.slug_field: data, "defaults": {"title": data}}
        obj, _ = qs.get_or_create(**params)
        return obj
