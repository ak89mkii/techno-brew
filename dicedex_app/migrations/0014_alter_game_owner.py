# Generated by Django 3.2.8 on 2022-09-01 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0013_remove_game_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='owner',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
