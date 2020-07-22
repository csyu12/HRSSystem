from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# 发送邮件，联系经纪人查询物业信息（不需要登录也可以发送邮件）
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # 检查用户是否已经询问过此房产
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, '关于`%s`房产，您已发送过邮件，请耐心等候房产经纪人答复' % listing)
                return redirect('listings:listing', listing_id)

        # 加入该用户的物业查询清单
        contact_obj = Contact(listing=listing, listing_id=listing_id, name=name,
                              email=email, phone=phone, message=message, user_id=user_id)
        contact_obj.save()

        # 暂时屏蔽邮件发送功能
        # send_mail(
        #     '房地产物业消息：',
        #     '有人询问' + listing + '的相关消息，请尽快回复！',
        #     'xxxx@qq.com',
        #     [realtor_email, 'xxxxx@yeah.net'],
        #     fail_silently=False
        # )

        messages.success(request, '您的请求已提交，房地产经纪人将尽快与您联系')

        return redirect('listings:listing', listing_id)
