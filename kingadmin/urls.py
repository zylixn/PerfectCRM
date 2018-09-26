from django.conf.urls import url
from kingadmin import views

urlpatterns = [
    url(r'^$', views.app_index,name='app_index'),
    url(r'^login/', views.acc_login,name='login'),
    url(r'^logout/', views.acc_logout,name='logout'),
    url(r'^(\w+)/(\w+)/', views.table_obj_list,name='table_obj_list'),
]
