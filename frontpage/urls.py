from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.landing_view, name='landing_view'),
]
