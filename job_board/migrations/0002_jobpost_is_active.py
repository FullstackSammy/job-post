# Generated by Django 4.2.7 on 2023-11-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]