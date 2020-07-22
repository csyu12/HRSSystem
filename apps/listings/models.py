from django.db import models
from apps.realtors.models import Realtor
import datetime, os


def save_img(instance, img_name):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    date_path = 'img/homes/' + date_str + '/'
    return os.path.join('static', date_path, img_name)


# 房屋列表
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, verbose_name='经纪人')
    title = models.CharField(max_length=200, verbose_name='标题')
    address = models.CharField(max_length=200, verbose_name='具体地址')
    city = models.CharField(max_length=100, verbose_name='所在城市')
    state = models.CharField(max_length=100, verbose_name='所在州')
    zipcode = models.CharField(max_length=20, verbose_name='邮政编码')
    description = models.TextField(blank=True, verbose_name='描述')
    price = models.IntegerField(verbose_name='价钱')
    bedrooms = models.IntegerField(verbose_name='睡房数量')
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='浴室数量')
    garage = models.IntegerField(default=0, verbose_name='车库数量')
    sqft = models.IntegerField(verbose_name='平方尺')
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='地皮尺寸')
    photo_main = models.ImageField(upload_to=save_img, verbose_name='主照片')
    photo_1 = models.ImageField(upload_to=save_img, blank=True, verbose_name='照片1')
    photo_2 = models.ImageField(upload_to=save_img, blank=True, verbose_name='照片2')
    photo_3 = models.ImageField(upload_to=save_img, blank=True, verbose_name='照片3')
    photo_4 = models.ImageField(upload_to=save_img, blank=True, verbose_name='照片4')
    photo_5 = models.ImageField(upload_to=save_img, blank=True, verbose_name='照片5')
    photo_6 = models.ImageField(upload_to=save_img, blank=True, verbose_name='照片6')
    is_published = models.BooleanField(default=True, verbose_name='出售')
    list_date = models.DateTimeField(default=datetime.datetime.now(), blank=True, verbose_name='创建日期')

    class Meta:
        verbose_name = verbose_name_plural = '房屋资料'

    def __str__(self):
        return self.title
