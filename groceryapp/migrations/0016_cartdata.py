# Generated by Django 5.1.2 on 2024-12-13 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0015_delete_cartdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(default=None, max_length=50)),
                ('productimage', models.FileField(default=None, upload_to='')),
                ('productprice', models.IntegerField(default=None)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceryapp.product')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='groceryapp.userregistration')),
            ],
        ),
    ]
