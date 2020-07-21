# Generated by Django 3.0.6 on 2020-06-26 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entry', '0006_auto_20200626_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Düzenleyen', to=settings.AUTH_USER_MODEL),
        ),
    ]
