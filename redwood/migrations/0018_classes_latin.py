# Generated by Django 3.0.3 on 2020-08-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('redwood', '0017_auto_20200813_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='latin',
            field=models.CharField(default='', max_length=100, verbose_name='拉丁名'),
        ),
    ]
