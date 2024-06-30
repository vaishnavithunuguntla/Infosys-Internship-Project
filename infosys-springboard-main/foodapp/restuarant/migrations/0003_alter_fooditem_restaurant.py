# Generated by Django 5.0.6 on 2024-05-26 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0002_fooditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_items', to='restuarant.restaurant'),
        ),
    ]