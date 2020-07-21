# Generated by Django 3.0.6 on 2020-07-19 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entry', '0012_remove_entry_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='username',
            field=models.ForeignKey(default='adam', on_delete=django.db.models.deletion.CASCADE, related_name='kullanıcıadı', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='oluşturan', to=settings.AUTH_USER_MODEL),
        ),
    ]