# Generated by Django 3.2.4 on 2021-06-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0003_auto_20210607_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=128),
        ),
    ]