# Generated by Django 3.0.2 on 2021-03-19 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20210320_0250'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
