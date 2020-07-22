from django.contrib import admin
from django.utils.html import format_html
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    # 设置列表显示的属性
    list_display = ['show_img', 'is_published', 'title', 'address', 'price', 'city',
                    'state', 'zipcode', 'bedrooms', 'bathrooms', 'garage',
                    'sqft', 'lot_size', 'list_date']
    # 设置允许搜索关键字
    search_fields = ['realtor', 'title', 'address', 'zipcode', 'price']
    # 排序，负号表示降序
    ordering = []
    # 设置可直接编辑的字段
    list_editable = ['is_published']
    # 列表分页，设置支持最大显示行
    list_per_page = 7
    # 设置支持进入编辑界面的字段，默认第一个字段
    list_display_links = ['title']

    # 设置编辑页显示的属性以及排序
    fields = ['is_published', 'realtor', 'title', 'address', 'price', 'city',
              'state', 'zipcode', 'bedrooms', 'bathrooms', 'garage',
              'sqft', 'lot_size', 'photo_main', 'description', 'list_date',
              'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']
    # 过滤器
    list_filter = ['realtor', 'city', 'state', 'price', 'is_published']
    # 按时间分层
    date_hierarchy = 'list_date'

    def show_img(self, listing):
        html = '<img style="width:73px;height:50px;" src="/media/%s">'\
               % listing.photo_main.__str__()
        return format_html(html)
    show_img.short_description = '照片'
