# Generated by Django 5.0.6 on 2024-06-09 09:57

import ckeditor.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterplan', '0001_initial'),
        ('project', '0002_alter_project_description_alter_project_project_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterplanDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilities', ckeditor.fields.RichTextField()),
                ('youtube_url', models.URLField(validators=[django.core.validators.URLValidator()])),
                ('image_floorplan', models.ImageField(upload_to='floorplans/')),
                ('masterplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterplan.masterplan')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'verbose_name': 'Masterplan Detail',
                'verbose_name_plural': 'Masterplan Details',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('masterplan_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='masterplanDetails.masterplandetails')),
            ],
        ),
    ]
