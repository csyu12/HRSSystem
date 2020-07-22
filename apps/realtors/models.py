from django.db import models
import datetime, os


def save_img(instance, img_name):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    date_path = 'realtors/' + date_str + '/'
    return os.path.join('img', date_path, img_name)


# 房地产经纪人
class Realtor(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名')
    photo = models.ImageField(upload_to=save_img, verbose_name='照片')
    description = models.TextField(blank=True, verbose_name='描述')
    phone = models.CharField(max_length=20, verbose_name='手机号')
    email = models.CharField(max_length=50, verbose_name='电子邮箱')
    is_mvp = models.BooleanField(default=False, verbose_name='VIP')
    hire_date = models.DateTimeField(default=datetime.datetime.now(), blank=True, verbose_name='雇佣日期')

    class Meta:
        verbose_name = verbose_name_plural = '经纪人清单'

    def __str__(self):
        return self.name
