# Generated by Django 3.2.8 on 2022-09-07 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dicedex_app', '0026_alter_game_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
