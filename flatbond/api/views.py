from django.shortcuts import render
from .models import Flatbond
from .serializers import FlatBondSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class FlatBondViews(APIView):
    def get(self, request, format=None):
        queryset = Flatbond.objects.all()
        serializer = FlatBondSerializer(queryset, many=True)
        result_data = serializer.data
        result = {'flatbond': result_data}
        return Response(result)


class FlatBondDetailView(APIView):

    def get(self, request, flatbond_id=None):

        try:
            flatbond = Flatbond.objects.get(pk=flatbond_id)
        except Flatbond.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = FlatBondSerializer(flatbond)
        result = serializer.data
        return Response(result)
