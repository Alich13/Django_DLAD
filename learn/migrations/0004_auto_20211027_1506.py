# Generated by Django 3.0.3 on 2021-10-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_auto_20211027_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='historique',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='historique',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
