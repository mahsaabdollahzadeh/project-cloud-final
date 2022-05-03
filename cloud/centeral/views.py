from django.shortcuts import render
from urllib import response
from .serializers import centeralSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import centeral,airplane
from .serializers import centeralSerializer
import requests
from django.db import connection

# Create your views here.


class centeralViewSet(viewsets.ViewSet) :
    def list(self, request):
        username = request.headers.get("username")
        token = request.headers.get("tocken")
        print(username)
        print(token)
        serializer = centeralSerializer(centeral, many=True)
        return response(serializer.data)


    def create(self, request):
        serializer = centeralSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  response(serializer.data,status=status.HTTP_201_CREATED )

    def reserve_fly(self, request):
        pass

    def filter(self, request):
        pass

    def get_planes_of_a_company(self, request):
        pass
