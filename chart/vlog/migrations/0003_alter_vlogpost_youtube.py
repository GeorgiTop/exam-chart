# Generated by Django 3.2.5 on 2021-08-04 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0002_auto_20210805_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlogpost',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
