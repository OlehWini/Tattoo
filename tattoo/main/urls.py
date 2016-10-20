from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/', views.blog_page, name='blog_page'),
    url(r'^shop/', views.shop_page, name='shop_page'),
    url(r'^masters/', views.masters_page, name='masters_page'),
    url(r'^home/', views.index, name='index'),
    url(r'^search_master/', views.search_master, name='searching'),
    url(r'^topic_(\d+)/', views.topic_blog_page, name='topic_block_page'),
    url(r'^topic_(\d+)/add_comment', views.add_record, name='add_record'),
]
# https://www.youtube.com/watch?v=QgdINlxm-wE&list=PLpTASIMYgCp8supkEmnnrYa5xi9g91ZPI