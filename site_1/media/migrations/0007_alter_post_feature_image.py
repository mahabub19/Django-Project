# Generated by Django 4.1.5 on 2023-12-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_alter_post_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(blank=True, default='students.png', null=True, upload_to=''),
        ),
    ]