# Generated by Django 3.2 on 2022-02-27 18:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location_match', '0004_alter_locations_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='liked_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
