# Generated by Django 3.1.2 on 2022-09-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default/default-profile-logo.jpeg', upload_to='profile_image/%Y/%m/%d', verbose_name='Profile Image'),
        ),
    ]
