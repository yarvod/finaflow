from django.urls import path

from finances.views import OperationViewSet, CategoryViewSet, SourceOfIncomeViewSet

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
        "category/",
        OperationViewSet.as_view({"get": "list", "post": "create"}),
        name="category-list-create",
    ),
    path(
        "category/<str:pk>/",
        CategoryViewSet.as_view({"put": "partial_update", "delete": "destroy"}),
        name="category-update-destroy",
    ),
    path(
        "source/",
        SourceOfIncomeViewSet.as_view({"get": "list", "post": "create"}),
        name="source-list-create",
    ),
    path(
        "source/<str:pk>/",
        SourceOfIncomeViewSet.as_view({"put": "partial_update", "delete": "destroy"}),
        name="source-update-destroy",
    ),
]
