# Generated by Django 3.0.3 on 2021-10-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_historique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historique',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
