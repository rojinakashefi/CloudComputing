# from django.conf.urls import url
from django.urls import path, include
from .views import ad_api_view

urlpatterns = [path('api', ad_api_view.as_view())]
