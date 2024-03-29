# Generated by Django 5.0.1 on 2024-01-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0046_remove_item_event_remove_item_wishlist_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(default='None', max_length=1000, verbose_name='Description (Link Share) '),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Inventory', 'Inventory'), ('Link', 'Link'), ('Tracker', 'Personal Equipment Tracker'), ('Wishlist', 'Public Supply Wishlist'), ('Tool', 'Tool')], default='Inventory', max_length=30),
        ),
    ]
