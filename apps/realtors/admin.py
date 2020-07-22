from django.contrib import admin
from .models import Realtor
from django.utils.html import format_html


# Register your models here.
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    # 设置列表显示的属性
    list_display = ['show_img', 'name', 'phone', 'email', 'is_mvp', 'hire_date']
    # 设置允许搜索关键字
    search_fields = ['name', 'phone', 'email']
    # 排序，负号表示降序
    ordering = ['phone']
    # 设置可直接编辑的字段
    list_editable = []
    # 列表分页，设置支持最大显示行
    list_per_page = 7
    # 设置支持进入编辑界面的字段，默认第一个字段
    list_display_links = ['name']

    # 设置编辑页显示的属性以及排序
    fields = ['name', 'photo', 'phone', 'email', 'is_mvp', 'description', 'hire_date']

    # 过滤器
    list_filter = ['is_mvp']
    # 按时间分层
    date_hierarchy = 'hire_date'

    actions_on_bottom = True  # 底部显示删除动作选项
    actions_on_top = False  # 删除头部动作选项

    def show_img(self, realtor):
        html = '<img style="width:73px;height:50px;" src="/%s">'\
               % realtor.photo.__str__()
        return format_html(html)
    show_img.short_description = '照片'
