from django.shortcuts import render
from apps.listings.choices import price_choices, bedroom_choices, state_choices
from apps.listings.models import Listing
from apps.realtors.models import Realtor


# 首页
def index(request):
    # 从数据库获取房产清单
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)


# 关于我们
def about(request):
    # 获取所有经纪人信息
    realtors = Realtor.objects.order_by('-hire_date')

    # 获取VIP经纪人
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
