# Generated by Django 5.0.6 on 2024-06-12 09:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teammember', '0008_remove_videoaboutus_video_videoaboutus_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='description_one',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='description_two',
        ),
        migrations.RemoveField(
            model_name='ceoaboutus',
            name='description_one',
        ),
        migrations.RemoveField(
            model_name='ceoaboutus',
            name='description_two',
        ),
        migrations.RemoveField(
            model_name='videoaboutus',
            name='description_one',
        ),
        migrations.RemoveField(
            model_name='videoaboutus',
            name='description_two',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ceoaboutus',
            name='description',
            field=ckeditor.fields.RichTextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videoaboutus',
            name='description',
            field=ckeditor.fields.RichTextField(default=2),
            preserve_default=False,
        ),
    ]
