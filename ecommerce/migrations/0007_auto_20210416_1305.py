# Generated by Django 3.1.7 on 2021-04-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_auto_20210408_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(null=True, upload_to='static/userimage'),
        ),
    ]
