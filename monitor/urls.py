from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test$', views.testview, name='testview'),
    url(r'^home$', views.home, name='home'),
    url(r'^stats/hourly$', views.hourly, name='hourly')
 ]