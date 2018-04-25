from demo import models
from demo import serializers
from rest_framework import viewsets


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
