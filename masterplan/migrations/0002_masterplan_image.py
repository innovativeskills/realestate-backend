# Generated by Django 5.0.6 on 2024-06-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterplan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterplan',
            name='image',
            field=models.ImageField(default=1, upload_to='Masterplan/'),
            preserve_default=False,
        ),
    ]
