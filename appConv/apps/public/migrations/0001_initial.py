# Generated by Django 4.2.7 on 2023-12-18 05:33

import apps.public.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='logo', max_length=128, unique=True, verbose_name='Logo')),
                ('image', models.ImageField(upload_to=apps.public.models.Logo.change_name)),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logos',
            },
        ),
    ]
