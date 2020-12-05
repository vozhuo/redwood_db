from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Classes)
admin.site.register(models.Filters)

admin.site.site_header = '数据库管理后台'
admin.site.site_title = '数据库管理后台'

# pyinstaller manage.spec
