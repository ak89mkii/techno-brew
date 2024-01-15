# Generated by Django 5.0.1 on 2024-01-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0041_rename_genre_item_label_remove_item_coffee_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(choices=[('border-dark', 'White'), ('border-dark bg-warning', 'Yellow'), ('border-dark bg-info', 'Light Blue'), ('text-white bg-dark', 'Black')], default='border-dark', max_length=30),
        ),
    ]