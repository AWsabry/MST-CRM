# Generated by Django 5.0.1 on 2024-02-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations_and_services', '0002_remove_projects_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizations',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
