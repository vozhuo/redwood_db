# Generated by Django 2.2.1 on 2019-08-19 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redwood', '0008_auto_20190819_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='name',
        ),
    ]
