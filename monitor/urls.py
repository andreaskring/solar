from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test$', views.testview, name='testview'),
    url(r'^home$', views.home, name='home'),
    url(r'^stats/downtime/form$', views.downtime_form, name='downtime_form'),
    url(r'^stats/downtime/data$', views.downtime_data, name='downtime_data')
 ]