import uuid

from django.db import models
from django.utils.timezone import now

from common.constants import Currency, OperationType


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
    title = models.CharField(max_length=155, verbose_name="Название")
    slug = models.SlugField(verbose_name="Слаг")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class SourceOfIncome(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    user = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    title = models.CharField(max_length=155, verbose_name="Название")

    class Meta:
        verbose_name = "Источник дохода"
        verbose_name_plural = "Источники дохода"

    def __str__(self):
        return self.title


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
    title = models.CharField(max_length=155, verbose_name="Название")
    money = models.FloatField(default=0, verbose_name="Сумма денег")
    currency = models.IntegerField(choices=Currency.Choices, default=Currency.RUB, verbose_name="Валюта")
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория",
    )
    date = models.DateField(default=now, verbose_name="Дата")

    source_of_income = models.ForeignKey(
        "SourceOfIncome",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Источник дохода",
    )

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
        ordering = ["-date"]

    def __str__(self):
        return self.title
