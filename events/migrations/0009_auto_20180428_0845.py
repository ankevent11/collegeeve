# Generated by Django 2.0.4 on 2018-04-28 08:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20180428_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=tinymce.models.HTMLField(verbose_name='Details'),
        ),
    ]
