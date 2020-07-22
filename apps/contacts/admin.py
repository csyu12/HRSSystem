from django.contrib import admin
from django.utils.html import format_html
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # 设置列表显示的属性
    list_display = ['listing_id', 'listings_href', 'name', 'email',
                    'phone', 'message', 'contact_date']
    # 设置允许搜索关键字
    search_fields = ['name', 'listing_id', 'listing', 'phone']
    # 排序，负号表示降序
    ordering = []
    # 设置可直接编辑的字段
    list_editable = []
    # 列表分页，设置支持最大显示行
    list_per_page = 10
    # 设置支持进入编辑界面的字段，默认第一个字段
    list_display_links = ['name']

    # 设置编辑页显示的属性以及排序
    # fields = ['is_published', 'realtor', 'title', 'address', 'price', 'city',
    #           'state', 'zipcode', 'bedrooms', 'bathrooms', 'garage',
    #           'sqft', 'lot_size', 'description', 'list_date',
    #           'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']
    # 过滤器
    list_filter = ['name', 'listing_id', 'listing']
    # 按时间分层
    date_hierarchy = 'contact_date'

    def listings_href(self, contact):
        href = '/admin/listings/listing/?listing_id=%s' % contact.listing_id
        html = '<a href="%s">%s</a>' % (href, contact.listing)
        return format_html(html)
    listings_href.short_description = '房产标题'
