from rest_framework.serializers import ModelSerializer

from .models import Category

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name'
        )
        