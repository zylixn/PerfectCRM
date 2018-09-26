#-*-coding:utf-8-*-
#!/usr/bin/env python

from django.conf.urls import url
from django.contrib import admin
from crm import views

urlpatterns = [
    url(r'^$', views.dashboard,name="sales_dashboard"),
    url(r'^(\w+)/(\w+)/$', views.table_obj_list,name='table_obj_list'),
]