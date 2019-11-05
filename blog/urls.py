from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path(r'^post/new/$', views.post_new, name='post_new'),
    path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
