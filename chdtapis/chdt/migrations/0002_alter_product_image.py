# Generated by Django 5.1 on 2024-09-10 16:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chdt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
