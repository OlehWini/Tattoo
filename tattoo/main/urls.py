from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/', views.blog_page, name='blog_page'),
    url(r'^shop/', views.shop_page, name='shop_page'),
    url(r'^masters/', views.masters_page, name='masters_page'),
    url(r'^home/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^registration/', views.regist_new_user, name='registration'),
    url(r'^search_master/', views.search_master, name='searching'),
]
