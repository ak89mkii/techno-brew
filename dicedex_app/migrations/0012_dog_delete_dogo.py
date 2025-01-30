# Generated by Django 5.0.1 on 2025-01-30 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0011_remove_dogo_d_member_remove_dogo_dog_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_id', models.CharField(default='None', max_length=100)),
                ('breed', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Pokemon', 'Pokemon'), ('Robot', 'Robot')], default='Dog', max_length=30)),
                ('dog_name', models.CharField(default='None', max_length=100)),
                ('title', models.CharField(default='None', max_length=100)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('last_printed', models.DateTimeField(default='2025-01-01')),
                ('hrf_date', models.DateField(default='2025-01-01')),
                ('d_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='dicedex_app.member')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Dogo',
        ),
    ]
