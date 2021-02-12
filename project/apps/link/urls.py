from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('/send_email', views.send_email, name = 'send_email'),
    url(r'\w+', views.index, name='index'),
    url(r'', views.main, name='main'),
    
]
