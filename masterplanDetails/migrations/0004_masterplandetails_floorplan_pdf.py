# Generated by Django 5.0.6 on 2024-06-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterplanDetails', '0003_masterplandetails_facilities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterplandetails',
            name='floorplan_pdf',
            field=models.FileField(default=1, upload_to='floorplan/'),
            preserve_default=False,
        ),
    ]
