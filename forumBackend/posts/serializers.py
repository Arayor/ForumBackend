from rest_framework import serializers 
from posts.models import Post
from posts.models import Comment
 
class PostSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'content',
                  'created_at',
                  'updated_at',
                  'deleted_at')

class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = ('id',
                  'content',
                  'created_at',
                  'updated_at',
                  'deleted_at',
                  'post')