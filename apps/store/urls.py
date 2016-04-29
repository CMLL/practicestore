# -*- encoding:utf-8 -*-
from django.conf.urls import url
from ..store import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]