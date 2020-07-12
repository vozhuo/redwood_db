from django.db import models

# Create your models here.


class Classes(models.Model):
    desc = models.CharField(max_length=200, verbose_name='描述')
    type = models.CharField(max_length=20, verbose_name='类别')

    class Meta:
        verbose_name = "红木种类"
        verbose_name_plural = verbose_name


class Images(models.Model):
    redwood = models.ForeignKey(Classes, on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name = "红木图片"
        verbose_name_plural = verbose_name
