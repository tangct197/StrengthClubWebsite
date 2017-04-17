from django.conf.urls import url
from join import views

urlpatterns = [
    url(r'^$', views.join, name='join'),
]
