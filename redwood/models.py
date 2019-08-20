from django.db import models

# Create your models here.


class Redwood(models.Model):
    desc = models.CharField(max_length=200, verbose_name='描述')

    class Meta:
        verbose_name = "红木"
        verbose_name_plural = verbose_name


class Images(models.Model):
    redwood = models.ForeignKey(Redwood, on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name
