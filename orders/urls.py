from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import ordersViewSet, ordersList, ordersDetail

urlpatterns = [
    path('',ordersList.as_view()),
    path('<int:pk>/', ordersDetail.as_view()),
]