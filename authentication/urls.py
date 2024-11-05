# urls.py
from django.urls import path
from .views import CustomTokenObtainPairView,LogoutView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    
    path('token/', CustomTokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),    
    path('signout/',LogoutView.as_view(), name='signout'),

    ]
