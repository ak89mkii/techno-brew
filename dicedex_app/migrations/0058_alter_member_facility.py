# Generated by Django 5.0.1 on 2025-01-24 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0057_rename_facillity_name_facility_facility_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicedex_app.facility'),
        ),
    ]
