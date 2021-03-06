"""react_dajngo_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from api.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^SnippetList/', SnippetList.as_view()),
    url(r'^Login/', Login.as_view()),
    url(r'^Regiser/', Regiser.as_view()),
    url(r'^GetImgsList/', GetImgsList.as_view()),
    url(r'^GetWeather/', GetWeather.as_view()),
    url(r'^DelImage/', DelImage.as_view()),
    url(r'^upload/$', upload, name='upload'),
    url(r'^Dash/', Dash.as_view()),
    url(r'^comment/', Comment.as_view()),
    url(r'^getAvatar/', getAvatar, name='getAvatar'),
]
