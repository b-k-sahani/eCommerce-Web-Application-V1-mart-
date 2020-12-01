
from django.contrib import admin
from app.api.views import ProCRUD
from django.urls import path,include
#ROUTER
from rest_framework import routers
router=routers.DefaultRouter()
router.register('api',ProCRUD)
#TOKEN
from rest_framework.authtoken import views
from rest_framework_jwt import views

urlpatterns = [
    path('',include(router.urls)),
    #TOKEN AUTHENTICATION
    # path('get-api-token/',views.obtain_auth_token),
    #JWT
    path('auth-jwt/',views.obtain_jwt_token),
    path('auth-jwt-refresh/',views.refresh_jwt_token),
    path('auth-jwt-verify/',views.verify_jwt_token),
]
