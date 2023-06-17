from django.db.models import Q, Sum, F, Subquery
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

        expenditure_analytics = []
        expenditure_query = queryset.filter(type=OperationType.EXPENDITURE)
        for category in Category.objects.filter(
            user=request.user, type=OperationType.EXPENDITURE, parent__isnull=True
        ):
            parent_total = 0
            parent_expenditure = expenditure_query.filter(category=category)
            if parent_expenditure.exists():
                parent_total = (
                    parent_expenditure.aggregate(total=Coalesce(Sum("money"), 0.0))
                    .get("total", 0)
                )

            children_total = 0
            children_expenditure = expenditure_query.filter(category__parent=category)
            if children_expenditure.exists():
                children_total = (
                    children_expenditure.aggregate(total=Coalesce(Sum("money"), 0.0))
                    .get("total", 0)
                )
            print(children_expenditure.aggregate(total=Coalesce(Sum("money"), 0.0)))

            if parent_total > 0 or children_total > 0:
                expenditure_analytics.append(
                    {
                        "category": category.title,
                        "category_id": category.id,
                        "total": parent_total + children_total,
                    }
                )

        revenue_analytics = []
        revenue_query = queryset.filter(type=OperationType.REVENUE)
        for category in Category.objects.filter(
            user=request.user, type=OperationType.REVENUE, parent__isnull=True
        ):
            parent_total = 0
            parent_revenue = revenue_query.filter(category=category)
            if parent_revenue.exists():
                parent_total = (
                    parent_revenue.aggregate(total=Coalesce(Sum("money"), 0.0))
                    .get("total", 0)
                )

            children_total = 0
            children_revenue = revenue_query.filter(category__parent=category)
            if children_revenue.exists():
                children_total = (
                    children_revenue.aggregate(total=Coalesce(Sum("money"), 0.0))
                    .get("total", 0)
                )

            if parent_total > 0 or children_total > 0:
                revenue_analytics.append(
                    {
                        "category": category.title,
                        "category_id": category.id,
                        "total": parent_total + children_total,
                    }
                )

        revenue_analytics.sort(key=lambda x: x.get("total", 0), reverse=True)
        expenditure_analytics.sort(key=lambda x: x.get("total", 0), reverse=True)

        data = {
            "spent": spent.get("spent"),
            "earned": earned.get("earned"),
            "spent_by_category": expenditure_analytics,
            "earned_by_category": revenue_analytics,
        }
        return Response(data=data, status=200)

    @action(detail=False)
    def results(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        months = list(range(1, 13))
        total_spent = queryset.filter(type=OperationType.EXPENDITURE).aggregate(
            spent=Coalesce(Sum("money"), 0.0)
        )
        total_earned = queryset.filter(type=OperationType.REVENUE).aggregate(
            earned=Coalesce(Sum("money"), 0.0)
        )
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
        indexes_to_drop = [
            i
            for i, earned, spent in zip(range(12), format_earned, format_spent)
            if earned == 0 and spent == 0
        ]
        format_earned = [
            money for i, money in enumerate(format_earned) if i not in indexes_to_drop
        ]
        format_spent = [
            money for i, money in enumerate(format_spent) if i not in indexes_to_drop
        ]
        months = [month for i, month in enumerate(months) if i not in indexes_to_drop]
        return Response(
            status=200,
            data=dict(
                spent=format_spent,
                earned=format_earned,
                labels=months,
                total_spent=total_spent.get("spent", 0),
                total_earned=total_earned.get("earned", 0),
            ),
        )
