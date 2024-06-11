# Generated by Django 5.0.6 on 2024-06-11 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_v1", "0003_remove_cart_product_cart_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
        migrations.AddField(
            model_name="cart",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api_v1.product",
                verbose_name="Товар",
            ),
        ),
    ]
