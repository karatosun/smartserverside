# Generated by Django 3.0.6 on 2020-07-19 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0011_entry_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='created_by',
        ),
    ]
