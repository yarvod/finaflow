from django.contrib import admin

from finances.models import Operation, Category, SourceOfIncome


@admin.register(SourceOfIncome)
class SourceOfIncomeAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug",)


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "category", "money", "date")
    list_filter = ("type", "category",)
