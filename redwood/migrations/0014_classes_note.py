# Generated by Django 3.0.3 on 2020-08-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('redwood', '0013_auto_20200801_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='note',
            field=models.CharField(default='', max_length=200, verbose_name='注释'),
        ),
    ]
