from django.urls import path,include, re_path
from . import views
from django.shortcuts import render, get_object_or_404

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^index', views.index, name='index'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^China', views.China, name='China'),
    re_path(r'^Japan', views.Japan, name='Japan'),
    re_path(r'^game', views.game, name='game'),




]
