# Generated by Django 2.1.3 on 2018-12-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../media/%Y/%m/%D/'),
        ),
    ]