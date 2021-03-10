from rest_framework import serializers
from .models import *

class timingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timing
        fields=['id','timing1','timing2','user','status']

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields=['id','name','email','designation','number','timings']

class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields='__all__'