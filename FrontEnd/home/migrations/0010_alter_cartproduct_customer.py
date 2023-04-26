# Generated by Django 4.2 on 2023-04-17 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0009_cartproduct"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartproduct",
            name="customer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer_product",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]