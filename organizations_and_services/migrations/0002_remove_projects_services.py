# Generated by Django 5.0.1 on 2024-02-06 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations_and_services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='services',
        ),
    ]
