from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^flatbond/(?P<flatbond_id>\d+)',
                        views.FlatBondDetailView.as_view(), name="flatbond_detail"),
                        
    url(r'^flatbond', views.FlatBondViews.as_view(), name="flatbond_list"),
]