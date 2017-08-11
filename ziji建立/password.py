# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from forms import *
from usr.models import auth
from django.contrib.auth.decorators import login_required,permission_required

# 注册。。。。。。。。。。。。。。。。
@permission_reqired('add_User', login_url = '/login/')
def thanks(request):
    return HttpTesponse("感谢你的登入")

# @permission_reqired(login_url = '/thanks/')
def reg(request):
    try:
        if request.method == "POST":
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                cd = reg_form.cleaned_data
                User.objects.create(username = cd['username'], password = make_password(cd['password']), email = cd['email'], mobile = cd['tel'])
                return HttpResponseRedirect('/login/')
            else:
                return render(request,'failure.html',{'reason':reg_form.errors})
        else:
            reg_form = regForm()
    except Exception as e:
        print e
    return render(requeset,'reg.html',locals())


    @login_required(login_url = '/login/')
    def login_test(request):
        return HttpResponse('欢迎登入')

    def login(request):
        errors = []
        if request.method == "POST":
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            if not username:
                errors.append('Enter a username')
            if not password:
                errors.append('Enter a password')
            if not errors:
                if not request.user.is_authenticated():
                    user = auth.authenticate(username = username,password = password)
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                    else:
                        return HttpResponse('用户名或者密码错误')
                else:
                    return HttpResponse("你已经登入")
        return render(request, 'user_login.html',{'errors':errors})
