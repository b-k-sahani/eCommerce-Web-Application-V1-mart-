from app.models import ProductModel,UserModel
from app.models import UserModel,ProductModel
from rest_framework.serializers import ModelSerializer

class ProSerializers(ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'
