oot@CD-FTP-VPN:/opt/jastme# more jastme/settings.py

"""
Django settings for jastme project.

For more information on this file, see

For the full list of settings and their values, see

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r!1=i^3qhwglr(zf*9&n*ii!b_oy2h()ics(6(de3wuo0-oh8h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
#    'django.contrib.admin',                               #注释掉admin
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',                                #这个中间件是防止跨站攻击的。有意思的朋友可以去搜索下。
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jastme.urls'

WSGI_APPLICATION = 'jastme.wsgi.application'

# Database
# #databases

DATABASES = {                                   #数据库的相关配置
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'jastme',
        'USER':'jastme',
        'PASSWORD':'jastme',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# Internationalization
#

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
#

STATIC_URL = '/static/'

TEMPLATE_DIRS =(                                       #模板的路径
                '/var/www/jastme/',
)

views.py
root@CD-FTP-VPN:/opt/jastme# more login/views.py
from django.shortcuts import render
from django.contrib import auth
# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def my_login(request):                                #我们自定义一个函数，这个函数名字一定不要写成login，因为Django有有login模块。
    if request.method == 'POST':                      #我们使用POST的方法来获取从HTML传递过来的表单内容
        username = request.POST['username']           #获取账号和密码
        password = request.POST['password']
        user = authenticate(username=username, password=password)            #我们用user来实例化 authenticate(username=username, password=password)
        if user is not None:                     #用户名不为空
            if user.is_active:                   #为激活用户
                login(request, user)             #调用django.contrib.auth中的login函数，可以具体去看看源码
                return HttpResponseRedirect('/main')         #登陆成功就重定向到主页
        else:
            login_error = 'login error.'
            return render_to_response('login.html', {'login_error' : login_error, 'is_display' : 'display:block'})    #失败则返回登陆页面
    return render_to_response('login.html', {'is_display' : 'display:none'})    #同理

@login_required                       #调用了这个修饰器，就可以让这个页面在成功登陆后才能访问
def main(request):
    return HttpResponse('login sucess')          #直接返回这个字符串

再看看urls.py
root@CD-FTP-VPN:/opt/jastme# more jastme/urls.py
from django.conf.urls import patterns, include, url
#from django.contrib import admin
from login.views import my_login,main                           #这里是我们导入的项目中的views.py中的模块，就是我们自己写的函数
#from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jastme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
    (r'^main/$',main),
    (r'^login/$',my_login),

)

login.html
root@CD-FTP-VPN:/var/www/jastme# pwd
/var/www/jastme
root@CD-FTP-VPN:/var/www/jastme# ls
login.html

<form action="" method="POST">                  #在此页面以POST的方式来提交参数
<input type=text name="username">
<input type=text name="password">
<input type=submit value="send">
</form>
