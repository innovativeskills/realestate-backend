# Generated by Django 5.0.6 on 2024-06-10 12:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]