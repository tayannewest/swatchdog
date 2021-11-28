# Generated by Django 3.2.7 on 2021-11-28 03:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_photo_artsupply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artsupply',
            name='familiarity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Familiarity on a scale of 0 (first time using this material) to 5 (Regular professional use)'),
        ),
    ]
