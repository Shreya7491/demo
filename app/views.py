from rest_framework import generics

from . import models
from . import serializers
import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import StartSerializer,IdentifySerializer,ShowSerializer
from . models import Start,Random_No,Identify,Show, Random
from django.http import HttpResponse

from django.utils.crypto import get_random_string

class QuestionListView(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionListView


@api_view(['GET', 'POST'])
def start(request):
    if request.method == 'GET':
        ready=Start.objects.all()
        serializer = StartSerializer(ready,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StartSerializer(data=request.data)
        if serializer.is_valid():
            # name=serializer.data.get('name')
            # student_no=serializer.data.get('student_no')
            # return Response({'message':message})
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def generate(request):
    for i in range(10):
        unique_id=Random_No()
        unique_id.random = get_random_string(length=8)
        unique_id.save()
    return HttpResponse("hello world")

def generateshow(request):
    for i in range(10):
        unique=Random()
        unique.random_no = get_random_string(length=6)
        unique.save()
    return HttpResponse("hello world show")


@api_view(['GET', 'POST'])
def identify(request):
    if request.method == 'GET':
        ready=Identify.objects.all()
        serializer = IdentifySerializer(ready,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IdentifySerializer(data=request.data)
        if serializer.is_valid():
            # name=serializer.data.get('name')
            # student_no=serializer.data.get('student_no')
            # return Response({'message':message})
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def show(request):
    if request.method == 'GET':
        ready=Show.objects.all()
        serializer = ShowSerializer(ready,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            # name=serializer.data.get('name')
            # student_no=serializer.data.get('student_no')
            # return Response({'message':message})
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
