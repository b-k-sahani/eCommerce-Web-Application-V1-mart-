# Generated by Django 3.0.8 on 2020-09-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_usermodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='jdate',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='photo',
            field=models.ImageField(default=False, upload_to='user_images/'),
        ),
    ]
