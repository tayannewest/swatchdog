# Generated by Django 3.2.7 on 2021-11-29 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_artsupply_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='artsupply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.artsupply'),
        ),
    ]
