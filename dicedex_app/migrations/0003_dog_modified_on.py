# Generated by Django 5.0.1 on 2025-01-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0002_remove_dog_modified_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
