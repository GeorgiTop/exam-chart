# Generated by Django 3.2.5 on 2021-08-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0005_auto_20210805_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlogpost',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
