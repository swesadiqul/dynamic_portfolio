# Generated by Django 4.1.3 on 2022-11-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinformation',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
