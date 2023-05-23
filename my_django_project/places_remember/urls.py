from django.urls import re_path
from django.contrib.auth import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add-memory/$', views.add_memory, name='add-memory'),
    re_path(r'^logout/$', views.logout, name='logout'),
]
