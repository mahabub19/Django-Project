# Generated by Django 4.1.5 on 2023-12-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_post_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]