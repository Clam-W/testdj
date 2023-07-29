from django.db import models

# Create your models here.

# 测试平台核心模型-- 拆解HR用例部分

class Config(models.Model):
    name = models.CharField(verbose_name='名称',max_length=128)
    base_url = models.CharField('IP/域名',max_length=256,)