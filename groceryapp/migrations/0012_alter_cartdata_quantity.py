# Generated by Django 5.1.2 on 2024-12-13 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0011_cartdata_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdata',
            name='quantity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='groceryapp.product_unit'),
        ),
    ]
