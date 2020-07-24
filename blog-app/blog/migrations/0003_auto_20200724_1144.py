# Generated by Django 3.0.8 on 2020-07-24 11:44

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200717_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_url',
            field=models.URLField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.handle_featured_image),
        ),
    ]
