# Generated by Django 3.0.8 on 2020-10-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20201027_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='portfolio/images/logo.png', upload_to='portfolio/images/'),
        ),
    ]