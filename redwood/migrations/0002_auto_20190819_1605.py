# Generated by Django 2.2.1 on 2019-08-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redwood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redwood',
            name='classes',
            field=models.IntegerField(unique=True),
        ),
    ]