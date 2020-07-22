from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from apps.contacts.models import Contact


# 用户注册
def register(request):
    if request.method == 'POST':
        # 获取form表单数据
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # 检查两次密码输入是否一致
        if password == password2:
            # 检查账户名是否已被使用
            if User.objects.filter(username=username).exists():
                messages.error(request, '账户名已被使用')
                return redirect('accounts:register')
            else:
                # 检查邮箱是否已被使用
                if User.objects.filter(email=email).exists():
                    messages.error(request, '注册邮箱已被使用')
                    return redirect('accounts:register')
                else:
                    # 注册成功
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # 写法一：注册完后自动登录，使用到了Django内置的auth.login
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, '注册成功，已自动登录')
                    # return redirect('pages:index')

                    # 写法二：注册完后跳转到登陆界面，用户输入用户名和密码登录
                    user.save()
                    messages.success(request, '注册成功')
                    return redirect('accounts:login')
        else:
            messages.error(request, '两次输入的密码不一致')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')


# 用户登录
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, '欢迎！%s' % username)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, '登录信息有误，请检查账户和密码')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


# 用户登出
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, '您已登出')
        return redirect('pages:index')


# 用户面板
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
