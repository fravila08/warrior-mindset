# Generated by Django 5.0.6 on 2024-06-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_alter_appuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
