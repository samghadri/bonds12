from django.shortcuts import render
from .models import Flatbond
from .serializers import FlatBondSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class FlatBondViews(APIView):
    def get(self, request, format=None):
        queryset = Flatbond.objects.all()
        serializer = FlatBondSerializer(queryset, many=True)
        result_data = serializer.data
        result = {'flatbond': result_data}
        return Response(result)