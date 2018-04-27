from demo import models
from demo import serializers
from rest_framework import viewsets


class TagViewSet(viewsets.ModelViewSet):
    """
    API view for Tag model.
    """
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API view for Category model.
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API view for Post model.
    """
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
