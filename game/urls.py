"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from learn import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'register', views.register_request, name="register"),
    url(r'login/', views.login_request, name='login'),
    url(r"logout", views.logout_request, name="logout"),
    url(r'^learn/', include('learn.urls', namespace="learn")), #les path de quiz/url.py préfixée par quiz/
    url(r'^admin/', admin.site.urls),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
