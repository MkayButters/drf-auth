from .models import Blog
from rest_framework.serializers import ModelSerializer

class BlogSerializer(ModelSerializer):
    class Meta:
        model = blog
        fields = ('id', 'name', 'purchaser', 'description')
