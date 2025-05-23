# Generated by Django 4.2.16 on 2025-02-21 18:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('users', models.ManyToManyField(blank=True, related_name='dashboards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
