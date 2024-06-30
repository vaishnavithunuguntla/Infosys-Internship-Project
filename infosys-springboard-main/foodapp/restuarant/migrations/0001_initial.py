# Generated by Django 5.0.6 on 2024-05-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
