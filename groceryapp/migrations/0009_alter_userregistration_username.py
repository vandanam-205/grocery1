# Generated by Django 5.1.2 on 2024-12-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0008_rename_cart_cartdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]