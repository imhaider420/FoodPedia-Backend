from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.http import HttpResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from .permissions import postsPermission
from .serializers import postsSerializer
from .models import postsModel
from rest_framework.pagination import PageNumberPagination


class postsViewSet(viewsets.ModelViewSet):
    queryset = postsModel.objects.all().order_by('id')
    serializer_class = postsSerializer    


class postsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [postsPermission]
    def get(self, request, format=None):
        q = models.Q()
        title = request.GET.get('title')
        

        if title is not None:
            q &= models.Q(title=title)
                
        posts = postsModel.objects.filter(q)

        paginator = PageNumberPagination()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(posts, request)
        serializer = postsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


    def post(self, request, format=None):
        serializer = postsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class postsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [postsPermission]
    @csrf_exempt
    def get_object(self, pk):
        try:
            return postsModel.objects.get(pk=pk)
        except postsModel.DoesNotExist:
            raise Http404
    
    @csrf_exempt
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = postsSerializer(post)
        return Response(serializer.data)


    @csrf_exempt
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = postsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def patch(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = postsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



 