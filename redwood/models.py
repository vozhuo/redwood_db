from django.db import models

# Create your models here.


class Classes(models.Model):
    type = models.CharField(max_length=20, verbose_name='类别')
    map = models.ImageField(default='', verbose_name='地图')
    level = models.CharField(default='', max_length=200, verbose_name='保护等级', blank=True)
    genus = models.CharField(default='', max_length=50, verbose_name='科属名', blank=True)
    location = models.CharField(default='', max_length=500, verbose_name='分布', blank=True)
    macro = models.CharField(default='', max_length=500, verbose_name='宏观构造特征', blank=True)
    micro = models.CharField(default='', max_length=500, verbose_name='微观构造特征', blank=True)
    density = models.CharField(default='', max_length=50, verbose_name='木材气干密度', blank=True)

    class Meta:
        verbose_name = "红木种类"
        verbose_name_plural = verbose_name


class Images(models.Model):
    redwood = models.ForeignKey(Classes, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='微观图片')

    class Meta:
        verbose_name = "红木图片"
        verbose_name_plural = verbose_name
