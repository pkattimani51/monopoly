# Generated by Django 3.0.2 on 2020-01-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20200122_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='password',
            field=models.IntegerField(default=9086),
        ),
    ]