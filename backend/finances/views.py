from django.db.models import Q, Sum, F
from django.db.models.functions import Coalesce
from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework as filters

from common.constants import OperationType
from finances.filters import CategoryFilterSet, OperationsFilterSet
from finances.serializers import (
    OperationListSerializer,
    CategorySmallGetSerializer,
    OperationWriteSerializer,
    CategoryWriteSerializer,
)
from finances.models import Operation, Category


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CategoryFilterSet

    def get_queryset(self):
        return Category.objects.filter(
            Q(user=self.request.user) | Q(user__isnull=True)
        ).filter(parent__isnull=True)

    def get_serializer_class(self):
        if self.action in ("update", "create"):
            return CategoryWriteSerializer
        return CategorySmallGetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OperationViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = OperationsFilterSet

    def get_queryset(self):
        return Operation.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return OperationListSerializer
        return OperationWriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False)
    def analytics(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        spent = queryset.filter(type=OperationType.EXPENDITURE).aggregate(
            spent=Coalesce(Sum("money"), 0.0)
        )
        earned = queryset.filter(type=OperationType.REVENUE).aggregate(
            earned=Coalesce(Sum("money"), 0.0)
        )
        return Response(data={**earned, **spent}, status=200)

    @action(detail=False)
    def results(self, request):
        queryset = self.get_queryset().filter(date__year=now().year)
        months = list(range(1, 13))
        spent = (
            queryset.filter(type=OperationType.EXPENDITURE)
            .annotate(month=F("date__month"))
            .values("month")
            .annotate(total=Sum("money"))
            .values("month", "total")
            .order_by("month")
        )
        earned = (
            queryset.filter(type=OperationType.REVENUE)
            .annotate(month=F("date__month"))
            .values("month")
            .annotate(total=Sum("money"))
            .values("month", "total")
            .order_by("month")
        )
        format_earned = [
            next((item["total"] for item in earned if item["month"] == month), 0)
            for month in months
        ]
        format_spent = [
            next((item["total"] for item in spent if item["month"] == month), 0)
            for month in months
        ]
        return Response(
            status=200,
            data=dict(spent=format_spent, earned=format_earned, labels=months),
        )
