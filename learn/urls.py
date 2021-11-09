from django.conf.urls import url
from django.urls import path
from . import views # import views so we can use them in urls.

app_name = 'learn'

urlpatterns = [
    url(r'^$', views.All_resources , name="resources"),
    url(r'^(?P<image_id>[0-9]+)/$', views.detail , name="detail"),
    url(r'^search/$', views.search , name="search"),
    path('data',views.autocomplete,name="autocomplete")
]