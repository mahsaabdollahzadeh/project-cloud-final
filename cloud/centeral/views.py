from django.shortcuts import render
from urllib import response
from .serializers import CenteralSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import centeral,airplane, transport
from .serializers import CenteralSerializer
import requests
from django.db import connection
from .models import centeral as Centeral


# Create your views here.


class centeralViewSet(viewsets.ViewSet) :
    def list(self, request):
        centeral = Centeral.objects.all()
        serializer = CenteralSerializer(centeral, many = True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CenteralSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(serializer.data,status=status.HTTP_201_CREATED )

    def filter(self, request):
        query = f"SELECT * FROM `centeral_centeral`"
        and_clause=[]
        for k in request.data :
             if k == "datetime" :
                 if request.data.get("datetime")!=None :
                     and_clause.append("`datetime` BETWEEN '%s' AND '%s'"%(request.data.get("datetime")[0],request.data.get("datetime")[1]))
                 elif k == "price" :
                     if request.data.get("price")!=None :
                        and_clause.append("`price` BETWEEN '%s' AND '%s'"%(request.data.get("price")[0],request.data.get("price")[1]))
                 else:
                    if request.data.get(k) != None :
                        and_clause.append("`%s` = '%s'" % (k,request.data.get(k)))
             if len(and_clause) > 0 :
                filter_q= query + " WHERE " + ' AND '.join(and_clause) + ";"
             else : 
                filter_q= query + ";"
                print(filter_q)
                centeral = Centeral.objects.raw(filter_q)
                centeral = Centeral.objects.all()
        serializer = CenteralSerializer(centeral, many = True)
        return Response(serializer.data)


    def reserve_fly(self, request,*args, **kwargs):
        centeral_id = request.data.get("centeral_id")
        centeral = Centeral.objects.raw(f"SELECT * FROM `centeral_centeral` WHERE `id` = '{centeral_id}'")
        centeral_reserved= centeral[0].reserved
        airplane_type = centeral[0].airplane_type
        centeral_capacity = airplane.objects.raw(f"SELECT * FROM `centeral_airplane` WHERE `plane` = '{airplane_type}'")[0].capacity
        if centeral_reserved < centeral_capacity :
              data = {
                    "id" :centeral[0].id,
                    "city_origin" : centeral[0].city_origin,
                    "airfield_origin" : centeral[0].airfield_origin,
                    "destination_city" : centeral[0].destination_city,
                    "destination_airport" : centeral[0].destination_airport,
                    "datetime" : centeral[0].datetime,
                    "price" : centeral[0].price,
                    "transport" : centeral[0].transport,
                    "centeral_class" : centeral[0].centeral_class,
                    "airplane_type" : centeral[0].airplane_type,
                    "reserved" : centeral[0].reserved+1,
                     }
              
              serializer = CenteralSerializer(instance=centeral.objects.get(id = centeral_id), data=data)
              return Response(serializer.data, status = status.HTTP_202_ACCEPTED)





    def get_planes_of_a_company(self, request):
         transport = request.data.get("carrier")
         cursor = connection.cursor()
         cursor.execute(f"SELECT DISTINCT `centeral_centeral`.`airplane_type` AS id FROM `centeral_centeral` WHERE `transport` = '{transport}'")
         data = cursor
         print(data)
         return Response(data)
