from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework as filters

from finances.filters import CategoryFilterSet
from finances.serializers import (
    OperationListSerializer,
    CategorySmallGetSerializer, OperationWriteSerializer,
)
from finances.models import Operation, Category


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CategoryFilterSet

    def get_queryset(self):
        return Category.objects.filter(Q(user=self.request.user) | Q(user__isnull=True)).filter(parent__isnull=True)

    def get_serializer_class(self):
        return CategorySmallGetSerializer


class OperationViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Operation.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return OperationListSerializer
        return OperationWriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
