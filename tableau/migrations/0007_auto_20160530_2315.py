# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 14:15
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tableau', '0006_remove_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image1',
            field=imagekit.models.fields.ProcessedImageField(upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image2',
            field=imagekit.models.fields.ProcessedImageField(upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image3',
            field=imagekit.models.fields.ProcessedImageField(upload_to='pic_folder/'),
        ),
    ]
