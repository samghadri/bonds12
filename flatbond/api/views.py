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
        
    def post(self, request, format=None):
        serializer = FlatBondSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlatBondDetailView(APIView):

    def get(self, request, flatbond_id=None):

        try:
            flatbond = Flatbond.objects.get(pk=flatbond_id)
        except Flatbond.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = FlatBondSerializer(flatbond)
        result = serializer.data
        return Response(result)



