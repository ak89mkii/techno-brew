# Generated by Django 3.2.8 on 2022-09-01 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0019_game_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='owner',
            new_name='user',
        ),
    ]