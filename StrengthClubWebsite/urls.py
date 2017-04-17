"""StrengthClubWebsite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

#For about page
urlpatterns += [
    url(r'^about/', include('about.urls')),
]

#For events page
urlpatterns += [
    url(r'^events/', include('events.urls')),
]

#For home page
urlpatterns += [
    url(r'^home/', include('home.urls')),
]

#For join page
urlpatterns += [
    url(r'^join/', include('join.urls')),
]

#For resources page
urlpatterns += [
    url(r'^resources/', include('resources.urls')),
]

#This will set your base url to /home/
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/home/', permanent=True)),
]
