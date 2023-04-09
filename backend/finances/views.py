from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from finances.serializers import (
    OperationSerializer,
    CategorySerializer,
)
from finances.models import Operation, Category


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.filter(Q(user=self.request.user) | Q(user__isnull=True))

    def get_serializer_class(self):
        return CategorySerializer


class OperationViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Operation.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return OperationSerializer
