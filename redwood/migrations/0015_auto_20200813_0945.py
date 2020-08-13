# Generated by Django 3.0.3 on 2020-08-13 01:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('redwood', '0014_classes_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='note',
        ),
        migrations.AddField(
            model_name='classes',
            name='density',
            field=models.CharField(default='', max_length=50, verbose_name='木材气干密度'),
        ),
        migrations.AddField(
            model_name='classes',
            name='genus',
            field=models.CharField(default='', max_length=50, verbose_name='科属名'),
        ),
        migrations.AddField(
            model_name='classes',
            name='level',
            field=models.CharField(default='', max_length=200, verbose_name='保护等级'),
        ),
        migrations.AddField(
            model_name='classes',
            name='location',
            field=models.CharField(default='', max_length=500, verbose_name='分布'),
        ),
        migrations.AddField(
            model_name='classes',
            name='macro',
            field=models.CharField(default='', max_length=500, verbose_name='宏观构造特征'),
        ),
        migrations.AddField(
            model_name='classes',
            name='micro',
            field=models.CharField(default='', max_length=500, verbose_name='微观构造特征'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='微观图片'),
        ),
    ]