# Generated by Django 3.0.6 on 2020-07-19 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0009_auto_20200719_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='created_by',
        ),
    ]
