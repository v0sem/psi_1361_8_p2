# Generated by Django 2.1.5 on 2019-10-06 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
