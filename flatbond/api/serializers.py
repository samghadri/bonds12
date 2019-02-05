from rest_framework import serializers
from .models import Flatbond



class FlatBondSerializer(serializers.ModelSerializer):
    
    membership_fee = serializers.IntegerField()
    fixed_memebership_fee_amount = serializers.IntegerField()

    class Meta:
        model = Flatbond
        fields = '__all__'
