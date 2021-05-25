from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import postsViewSet, postsList, postsDetail 


urlpatterns = [
    path('', postsList.as_view()),
    path('<int:pk>/', postsDetail.as_view())
]