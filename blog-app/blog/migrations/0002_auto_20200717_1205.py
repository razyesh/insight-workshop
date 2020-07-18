# Generated by Django 3.0.8 on 2020-07-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Blog List', 'verbose_name_plural': 'Blog Lists'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]