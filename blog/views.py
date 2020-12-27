from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from .serializers import BlogSerializer
from .permissions import IsPurchaserOrReadOnly

class Blog(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsPurchaserOrReadOnly,)
