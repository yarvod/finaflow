from django.contrib import admin

from finances.models import Operation, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "type",
        "parent",
        "user",
    )
    list_filter = ("type",)
    search_fields = ("title", "user", "parent")


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ("type", "category", "user", "money", "date", "comment")
    list_filter = ("type",)
    search_fields = ("category", "user", "comment", "money")
