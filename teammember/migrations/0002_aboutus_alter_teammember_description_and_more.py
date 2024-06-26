# Generated by Django 5.0.6 on 2024-06-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammember', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_one', models.CharField(max_length=500, verbose_name='Title One')),
                ('title_two', models.CharField(max_length=500, verbose_name='Title Two')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_us/', verbose_name='Image')),
                ('video', models.FileField(blank=True, null=True, upload_to='about_us/', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.AlterField(
            model_name='teammember',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='dribble_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Dribble Link'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Facebook Link'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(upload_to='teammember/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='instagram_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Instagram Link'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='linkedin_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='LinkedIn Link'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='twitter_link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Twitter Link'),
        ),
    ]
