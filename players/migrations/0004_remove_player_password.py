# Generated by Django 3.0.2 on 2020-01-22 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_player_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='password',
        ),
    ]
