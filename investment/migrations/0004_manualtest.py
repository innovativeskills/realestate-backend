# Generated by Django 5.0.6 on 2024-06-12 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0003_descriptioninvestmentone_descriptioninvestmentthree_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='investment/')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'ManualTest',
                'verbose_name_plural': 'ManualTest',
            },
        ),
    ]