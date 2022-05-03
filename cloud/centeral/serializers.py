from .models import centeral
from rest_framework import serializers

class centeralSerializer(serializers.ModelSerializer) :
    class Meta:
        model =centeral
        fields = '__all__'