from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from django.http import Http404
from django.http import HttpResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from .serializers import usersSerializer
from .models import usersModel
from .permissions import usersPermission
from rest_framework.pagination import PageNumberPagination



class usersViewSet(viewsets.ModelViewSet):
    queryset = usersModel.objects.all().order_by('id')
    serializer_class = usersSerializer


class usersList(APIView):

    permission_classes = [usersPermission]
    def get(self, request, format=None):
        q = models.Q()
        name = request.GET.get('name')
        phone= request.GET.get('phone')
        email= request.GET.get('email')
        area= request.GET.get('area')

        if name is not None:
            q |= models.Q(first_name__icontains=name)
            q |= models.Q(last_name__icontains=name)
        if phone is not None:
            q &= models.Q(phone_number__icontains=phone)
        
        if email is not None:
            q &= models.Q(email__icontains=email)
        if area is not None:
            q &= models.Q(area_id=area)

                
        users = usersModel.objects.filter(q)
        paginator = PageNumberPagination()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(users, request)
        serializer = usersSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class usersDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    @csrf_exempt
    def get_object(self, pk):
        try:
            return usersModel.objects.get(pk=pk)
        except usersModel.DoesNotExist:
            raise Http404

    @csrf_exempt
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = usersSerializer(user)
        if self.has_object_permission(request, user) == False:
            self.permission_denied(request)
        return Response(serializer.data)


    @csrf_exempt
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = usersSerializer(user, data=request.data)
        if self.has_object_permission(request, user) == False:
            self.permission_denied(request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @csrf_exempt
    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = usersSerializer(user, data=request.data)
        if self.has_object_permission(request, user) == False:
            self.permission_denied(request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        if self.has_object_permission(request, user) == False:
            self.permission_denied(request)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def has_object_permission(self, request, obj):
            if request.method == "DELETE":
                return request.user.is_superuser
            elif request.user == obj or request.user.is_superuser:
                return True
            else:
                return False
    
