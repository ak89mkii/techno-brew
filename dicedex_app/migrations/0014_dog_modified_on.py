# Generated by Django 5.0.1 on 2025-01-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0013_remove_dog_hrf_date_remove_dog_last_printed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
