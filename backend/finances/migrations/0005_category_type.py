# Generated by Django 3.2.9 on 2023-04-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0004_category_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="type",
            field=models.IntegerField(
                choices=[(1, "Расход"), (2, "Доход")],
                default=1,
                verbose_name="Тип категории",
            ),
        ),
    ]
