from django.conf.urls import url
from events import views

urlpatterns = [
    url(r'^$', views.events, name='events'),
]
