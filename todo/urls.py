from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^report/$', views.status_report, name='status_report'),
]
