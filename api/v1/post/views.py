from rest_framework import viewsets, response

from .serializers import PostOutputSerializer
from apps.post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.none()
    serializer_class = PostOutputSerializer
