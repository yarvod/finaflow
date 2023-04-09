import uuid

from django.db import models
from django.utils.timezone import now

from common.constants import Currency, OperationType
from finances.utils import iterate_parents, iterate_children, iterate_parents_titles


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    user = models.ForeignKey(
        to="users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Пользователь",
    )
    type = models.IntegerField(
        choices=OperationType.Choices,
        default=OperationType.EXPENDITURE,
        verbose_name="Тип категории",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="Родитель",
    )
    title = models.CharField(max_length=155, verbose_name="Название")
    slug = models.SlugField(verbose_name="Слаг")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def get_parents_ids(self):
        parents_ids = []
        iterate_parents(parents_ids, self)
        return parents_ids

    def get_categories_chain_titles(self):
        parents_titles = []
        iterate_parents_titles(parents_titles, self)
        parents_titles.reverse()
        parents_titles.append(self.title)
        return parents_titles

    def get_children_ids(self):
        children_ids = []
        iterate_children(children_ids, self)
        return children_ids


class Operation(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    user = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    type = models.IntegerField(
        choices=OperationType.Choices,
        default=OperationType.EXPENDITURE,
        verbose_name="Тип операции",
    )
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    money = models.FloatField(default=0, verbose_name="Сумма денег")
    currency = models.IntegerField(
        choices=Currency.Choices, default=Currency.RUB, verbose_name="Валюта"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория",
    )
    date = models.DateField(default=now, verbose_name="Дата")

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
        ordering = ["-date"]

    def __str__(self):
        if self.category:
            return ":".join(self.category.get_categories_chain_titles())
        return self.id
