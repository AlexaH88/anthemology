# Generated by Django 3.2.16 on 2023-01-12 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artwork',
        ),
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]