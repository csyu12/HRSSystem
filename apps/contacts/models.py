from django.db import models
import datetime


# 房产查询清单
class Contact(models.Model):
    listing = models.CharField(max_length=200, verbose_name='房产标题')
    listing_id = models.IntegerField(verbose_name='房产ID')
    name = models.CharField(max_length=200, verbose_name='查询人姓名')
    email = models.CharField(max_length=200, verbose_name='查询人邮箱')
    phone = models.CharField(max_length=200, verbose_name='查询人手机号')
    message = models.TextField(blank=True, verbose_name='留言')
    contact_date = models.DateTimeField(default=datetime.datetime.now(), blank=True, verbose_name='联系时间')
    user_id = models.IntegerField(default=-1, blank=True, verbose_name='查询人ID')     # -1代表用户未注册，直接与房产经纪人联系

    class Meta:
        verbose_name = verbose_name_plural = '查询清单'

    def __str__(self):
        return self.name
