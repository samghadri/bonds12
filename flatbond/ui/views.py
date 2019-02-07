from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class HomePage(TemplateView):
    template_name = "ui/index.html"


class FlatBondListView(TemplateView):
    template_name = "ui/flatbond.html"