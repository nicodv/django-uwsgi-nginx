from django.conf.urls import url
from helloworldapp import views

urlpatterns = [
    url(r'^/$', views.helloworld),
]
