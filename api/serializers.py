from rest_framework import serializers
from api.models import Snippet,CommentModel


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('id', 'uReply', 'uName', 'uComment', 'uUrl', 'uImg', 'uTime')
