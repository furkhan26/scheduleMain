from django.shortcuts import render
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *


class allData(generics.ListCreateAPIView):
    queryset = Timing.objects.all()
    serializer_class = timingSerializer

class action(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timing
    serializer_class = timingSerializer

class doctordata(generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = doctorSerializer

class doctoredit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctors
    serializer_class = doctorSerializer



# Create your views here.
# @api_view(['GET'])
# def get_all(request):
#     TimingData = Timing.objects.all()
#     All_Data = timingSerializer(TimingData,many=True) 
#     return Response(All_Data.data)

# @api_view(['GET'])
# def put(pk,request):
#     id = Timing.objects.get(id=pk)
#     serl = timingSerializer(id)
#     pass

# @api_view(['POST'])
# def createTodo(request):
#    serializer=timingSerializer(data=request.data)
#    if serializer.is_valid():
#       serializer.save()
#    return Response(serializer.data)