from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.http import HttpResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from .serializers import reviewsSerializer
from .models import reviewsModel
from .permissions import reviewsPermission

class reviewsViewSet(viewsets.ModelViewSet):
    queryset = reviewsModel.objects.all().order_by('id')
    serializer_class = reviewsSerializer


class reviewsList(APIView):

    permission_classes = [reviewsPermission]
    def get(self,request,format=None):
        q  = models.Q()
        user = request.GET.get('user_id')
        post = request.GET.get('post_id')

        if user is not None:
            q &= models.Q(user_id=user)
        if post is not None:
            q &= models.Q(post_id=post)

        reviews = reviewsModel.objects.filter(q)

        paginator = PageNumberPagination()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(reviews, request)
        serializer = reviewsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


    def post(self, request, format=None):
        serializer = reviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class reviewsDetail(APIView):

    @csrf_exempt
    def get_object(self, pk):
        try:
            return reviewsModel.objects.get(pk=pk)
        except reviewsModel.DoesNotExist:
            raise Http404


    @csrf_exempt
    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = reviewsSerializer(review)
        return Response(serializer.data)


    @csrf_exempt
    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = reviewsSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @csrf_exempt
    def patch(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = reviewsSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
         
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    