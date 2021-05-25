from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.http import HttpResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from .serializers import ordersSerializer
from .models import ordersModel
from .permissions import ordersPermission

from rest_framework.pagination import PageNumberPagination

class ordersViewSet(viewsets.ModelViewSet):
    queryset = ordersModel.objects.all().order_by('id')
    serializer_class = ordersSerializer


class ordersList(APIView):
    
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [ordersPermission]
    def get(self, request, format=None):
        q = models.Q()
        user = request.GET.get('user')
        area= request.GET.get('area')
        status= request.GET.get('status')
        start_date= request.GET.get('start_date')
        end_date= request.GET.get('end_date')

        if user is not None:
            q &= models.Q(user_id=user)
        if area is not None:
            q &= models.Q(area_id=area)

        if status is not None:
            q &= models.Q(status=status)
        
        if start_date is not None and end_date is not None: 
            q &= models.Q(created_at__range =[start_date,end_date])
        
        orders = ordersModel.objects.filter(q)
        
        paginator = PageNumberPagination()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(orders, request)
        serializer = ordersSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ordersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class ordersDetail(APIView):
    
    @csrf_exempt
    def get_object(self, pk):
        try:
            return ordersModel.objects.get(pk=pk)
        except ordersModel.DoesNotExist:
            raise Http404
    
    @csrf_exempt
    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = ordersSerializer(order)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = ordersSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def patch(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = ordersSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


