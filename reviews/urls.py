from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import reviewsViewSet, reviewsList, reviewsDetail

urlpatterns = [
    path('',reviewsList.as_view()),
    path('<int:pk>/', reviewsDetail.as_view()),
]