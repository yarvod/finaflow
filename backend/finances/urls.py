from django.urls import path

from finances.views import OperationViewSet, CategoryViewSet

urlpatterns = [
    path(
        "operation/",
        OperationViewSet.as_view({"get": "list", "post": "create"}),
        name="operation-list-create",
    ),
    path(
        "operation/<str:pk>/",
        OperationViewSet.as_view({"put": "partial_update", "delete": "destroy"}),
        name="operation-update-destroy",
    ),
    path(
        "analytics/",
        OperationViewSet.as_view({"get": "analytics"}),
        name="analytics",
    ),
    path(
        "results/",
        OperationViewSet.as_view({"get": "results"}),
        name="results",
    ),
    path(
        "category/",
        CategoryViewSet.as_view({"get": "list", "post": "create"}),
        name="category-list-create",
    ),
    path(
        "category/<str:pk>/",
        CategoryViewSet.as_view({"put": "partial_update", "delete": "destroy"}),
        name="category-update-destroy",
    ),
]
