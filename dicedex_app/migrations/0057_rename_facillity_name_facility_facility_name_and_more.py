# Generated by Django 5.0.1 on 2025-01-24 15:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0056_member_facility_dog'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='facility',
            old_name='facillity_name',
            new_name='facility_name',
        ),
        migrations.AlterField(
            model_name='member',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
