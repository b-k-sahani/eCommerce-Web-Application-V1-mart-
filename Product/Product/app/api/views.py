from django.shortcuts import render
from app.models import UserModel,ProductModel
from rest_framework.viewsets import ModelViewSet
from app.api.serializers import ProSerializers
# from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly


# Create your views here.
class ProCRUD(ModelViewSet):
    queryset=ProductModel.objects.all()
    serializer_class = ProSerializers
    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]
    #JWT
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated,]