# Generated by Django 3.1.7 on 2021-04-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BD_detection', '0002_auto_20210407_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_image',
            name='output_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='bd_image',
            name='post_image',
            field=models.ImageField(upload_to='upload2/'),
        ),
        migrations.AlterField(
            model_name='bd_image',
            name='pre_image',
            field=models.ImageField(upload_to='upload2/'),
        ),
    ]
