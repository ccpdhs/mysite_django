# -*- coding:utf-8 -*-
# Author : Dexter
# Data : 2018/8/16  下午10:41
from django.urls import path
from . import views


urlpatterns = [
    #loaclhost:8000/article/1
    path('<int:article_id>', views.article_detail, name="article_detail"),
    #loaclhost:8000/article/
    path('', views.article_list, name="article_list"),

    ]


