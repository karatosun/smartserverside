# Generated by Django 3.0.6 on 2020-07-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20200626_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='profile_picture',
            field=models.ImageField(blank=True, default='defaultpp.jpg', null=True, upload_to='profile_picture'),
        ),
    ]