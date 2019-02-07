from django.conf.urls import url
from . import views

urlpatterns = [
    url("^flatbond/$", views.FlatBondListView.as_view(), name="flatbond_lst"),
    url("^$", views.HomePage.as_view(), name="index"),
]