from rest_framework import serializers
from .models import Flatbond



class FlatBondSerializer(serializers.ModelSerializer):
    fixed_memebership_fee = serializers.BooleanField(default=False)
    membership_fee = serializers.ReadOnlyField()
    fixed_memebership_fee_amount = serializers.ReadOnlyField()
    rent = serializers.IntegerField()
    postcode = serializers.CharField(allow_null=True)
    is_monthly = serializers.BooleanField(default=False)


    class Meta:
        model = Flatbond
        fields = '__all__'
    
    def create(self, validated_data):
        return Flatbond.objects.create(**validated_data)
