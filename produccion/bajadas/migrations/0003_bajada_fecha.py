# Generated by Django 3.0.4 on 2020-04-22 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bajadas', '0002_remove_bajada_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='bajada',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
