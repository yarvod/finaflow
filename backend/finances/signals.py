import json

from django.db.models.signals import post_save
from django.dispatch import receiver

from finances.models import Category
from users.models import User


@receiver(post_save, sender=User)
def create_statistic(sender, instance, created, **kwargs):
    if created:
        with open("finances/fixtures/categories.json", "r", encoding="utf-8") as f:
            categories = json.load(f)
        for category in categories:
            Category.objects.create(
                user=instance,
                title=category["fields"]["title"],
                type=category["fields"].get("type", 1),
                parent_id=category["fields"].get("parent", None),
            )
