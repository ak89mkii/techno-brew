# Generated by Django 3.2.8 on 2022-08-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0003_alter_game_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='owner',
            field=models.CharField(default='IG88', max_length=100),
        ),
    ]