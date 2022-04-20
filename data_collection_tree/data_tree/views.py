from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Datatree
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_417_EXPECTATION_FAILED,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView
from django.db import connection
# Create your views here.


class DataInsert(CreateAPIView):
    def post(self, request):
        data = request.data
        dim=data.get('dim')
        metrics = data.get('metrics')
        device,country,webreq,timespent=None,None,None,None
        for element in dim:
            if element['key']=='device':
                device=element['val']
            elif element['key']=='country':
                country=element['val']
        
        for element in metrics:
            if element['key']=='webreq':
                webreq=element['val']
            elif element['key']=='timespent':
                timespent=element['val']
        
        DataTree.objects.create(device=device, country=country,webreq=webreq, timespent=timespent)
    
        return Response({"msg":"data inserted successfully","status":HTTP_200_OK})


class DataQuery(APIView):
    def post(self, request):
        dim=request.data['dim']
        device,country=None,None
        for element in dim:
            if element['key']=='country':
                country=element['val']
            # if element['key']=='device':
            #     device=element['val']
        cur = connection.cursor()
        query="SELECT country,SUM(webreq)webreq,SUM(timespent)timespent FROM DataTree order by country WHERE country='%s';",country
        cursor.execute(query)
        data = cursor.fetchall()
        return Response({"data": data,"status":HTTP_200_OK})
        
        
        
        