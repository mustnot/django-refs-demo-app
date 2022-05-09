from rest_framework import serializers

from apps.post.models import Post


class PostOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
