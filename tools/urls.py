from django.conf.urls import url
from tools import views

urlpatterns = [
    url(r'^$', views.tools, name='tools'),
]
