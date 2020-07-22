from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .choices import price_choices, bedroom_choices, state_choices
from .models import Listing


# 房产信息列表主页 eg: /listings
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # 每页显示3个
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)


# 房子详情页 eg: /listings/1
def listing(request, listing_id):
    # 用户直接输入不存在的房产ID，例如直接输入http://127.0.0.1/listings/1000
    # 使用Django内置方法get_object_or_404直接返回404即可
    listing_mes = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing_mes
    }

    return render(request, 'listings/listing.html', context)


# 搜索 /listings/search?keywords=&city=&price=
def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # 从房产描述中搜索关键字
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # 搜索城市
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # 搜索所在州
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # 搜索睡房数量
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)    # lte（小于或等于）

    # 搜索房产价格
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)    # lte（小于或等于）

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
