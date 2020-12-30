from .views import ListBlogPostsView, BlogRetrieveUpdateDestroy
from django.urls import path

urlpatterns = [
    path('', ListBlogPostsView.as_view(), name = 'all blog post'),
    path('<int:pk>', BlogRetrieveUpdateDestroy.as_view(), name = "destroy"),
]
