from .views import Blog

urlpatterns = [
    path('', Blog.as_view(), name = 'blog post'),
    path('<int:pk/>', BlogRetrieveUpdateDestroy.as_view(), name = "destroy"),
]
