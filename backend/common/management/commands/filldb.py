from django.core.management import BaseCommand

from common.constants import OperationType
from finances.models import Category, Operation
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        c1, _ = Category.objects.update_or_create(
            title="Еда, продукты",
        )
        c2, _ = Category.objects.update_or_create(
            title="Кафе, рестораны"
        )
        u1 = User.objects.filter(email="ivan@site.ru").first()
        if not u1:
            u1 = User.objects.create_user(
                username="ivan@site.ru",
                first_name="Иван",
                last_name="Иванов",
                email="ivan@site.ru",
                password="1111",
            )
            u1.save()
        c3, _ = Category.objects.update_or_create(
            title="Обучение", user=u1
        )
        o1, _ = Operation.objects.update_or_create(
            user=u1,
            title="Шаурма",
            defaults=dict(
                type=OperationType.EXPENDITURE,
                category=c1,
                money=200.2,
            ),
        )

        u2 = User.objects.filter(email="alex@site.ru").first()
        if not u2:
            u2 = User.objects.create_user(
                username="alex@site.ru",
                first_name="Алексей",
                last_name="Алексеев",
                email="alex@site.ru",
                password="1111",
            )
            u2.save()
