# Generated by Django 3.0.4 on 2020-04-22 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bajadas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bajada',
            name='fecha',
        ),
    ]
