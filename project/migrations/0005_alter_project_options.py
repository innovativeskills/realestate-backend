# Generated by Django 5.0.6 on 2024-06-12 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_description_project_description_one_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
