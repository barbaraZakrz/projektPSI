"""projektPSI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from django.urls import re_path
from szkola.views import *
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),

    path('KursList/', KursList.as_view()),
    path('KursDetails/<int:pk>', KursDetail.as_view()),

    path('UczenList/', UczenList.as_view()),
    path('UczenDetails/<int:pk>', UczenDetail.as_view()),

    path('DzienList/', DzienList.as_view()),
    path('DzienDetails/<int:pk>', DzienDetail.as_view()),

    path('RodzajList/', RodzajList.as_view()),
    path('RodzajDetails/<int:pk>', RodzajDetail.as_view()),

    path('Nauczyciel_RodzajList/', Nauczyciel_RodzajList.as_view()),
    path('Nauczyciel_RodzajDetails/<int:pk>', Nauczyciel_RodzajDetail.as_view()),




]

