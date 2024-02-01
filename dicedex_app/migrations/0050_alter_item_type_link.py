# Generated by Django 5.0.1 on 2024-02-01 15:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0049_item_label'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Inventory', 'Inventory'), ('Link', 'Link'), ('Tracker', 'Personal Equipment Tracker'), ('Wishlist', 'Public Supply Wishlist'), ('Tool', 'Tool')], default='Tool', max_length=30),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='None', max_length=1000, verbose_name='Description (Link Share) ')),
                ('link', models.CharField(default='None', max_length=1000, verbose_name='Link (Link Share)')),
                ('color', models.CharField(choices=[('border-dark', 'White'), ('border-dark bg-warning', 'Yellow'), ('border-dark bg-info', 'Light Blue'), ('text-white bg-dark', 'Black')], default='border-dark', max_length=30)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
