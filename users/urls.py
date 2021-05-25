from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import usersList, usersDetail
from .serializers import TokenObtainPairSerializer

urlpatterns = [
    # path('', include(router.urls)),
    #path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'), 
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('expire/', jwt_views.TokenRefreshView.as_view(), name='token_expire'),
    path('', usersList.as_view()),
    path('<int:pk>/', usersDetail.as_view()),
]