from django.contrib import admin

from finances.models import Operation, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "type",
        "parent",
    )
    list_filter = ("type",)


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ("type", "category", "money", "date", "comment")
    list_filter = (
        "type",
        "category",
    )
