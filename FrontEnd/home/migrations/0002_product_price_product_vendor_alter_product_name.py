# Generated by Django 4.2 on 2023-04-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name="product",
            name="vendor",
            field=models.CharField(default="Unknown", max_length=50),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(default="Unknown", max_length=50),
        ),
    ]
