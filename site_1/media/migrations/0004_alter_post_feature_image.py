# Generated by Django 4.1.5 on 2023-12-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_alter_post_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to=''),
        ),
    ]
