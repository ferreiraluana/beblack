# Generated by Django 4.2 on 2023-04-16 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_remove_product_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="imageUrl",
            field=models.CharField(default="", max_length=50),
        ),
    ]
