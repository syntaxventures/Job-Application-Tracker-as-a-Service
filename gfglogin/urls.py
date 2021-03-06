from django.contrib import admin
#from django.urls import path, include
from django.conf.urls import url, include
from gfgauth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('gfgauth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
]
