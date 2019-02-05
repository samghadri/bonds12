from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^flatbond', views.FlatBondViews.as_view(), name="flatbond_list"),
]