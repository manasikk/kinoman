# Generated by Django 3.2.13 on 2023-08-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=None, max_length=8),
        ),
    ]
