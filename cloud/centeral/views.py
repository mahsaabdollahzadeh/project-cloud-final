from django.shortcuts import render
from urllib import response
from .serializers import CenteralSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import centeral,airplane
from .serializers import CenteralSerializer
import requests
from django.db import connection
from .models import centeral as Centeral


# Create your views here.


class centeralViewSet(viewsets.ViewSet) :
    def list(self, request):
        centeral=Centeral.objects.all()
        Serializer=CenteralSerializer(Centeral)
        return Response(Serializer.data, many= True)

    def create(self, request):
        serializer = CenteralSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(serializer.data,status=status.HTTP_201_CREATED )

    def reserve_fly(self, request):
        pass

    def filter(self, request):
        pass

    def get_planes_of_a_company(self, request):
        pass
