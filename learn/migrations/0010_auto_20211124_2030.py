# Generated by Django 3.0.3 on 2021-11-24 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0009_auto_20211124_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Profile'),
        ),
    ]
