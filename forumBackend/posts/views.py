from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from datetime import datetime

from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view

#POSTS
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            posts = posts.filter(title__icontains=title)
        
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    try: 
        post = Post.objects.get(pk=id) 
    except Post.DoesNotExist: 
        return JsonResponse({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        post_serializer = PostSerializer(post) 
        return JsonResponse(post_serializer.data) 
 
    elif request.method == 'PUT': 
        post_data = JSONParser().parse(request) 
        post_data['updated_at'] = datetime.now()
        post_serializer = PostSerializer(post, data=post_data)

        if post_serializer.is_valid(): 
            post_serializer.save() 
            return JsonResponse(post_serializer.data) 
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        post.delete() 
        return JsonResponse({'message': 'Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

#COMMENTS
@api_view(['GET', 'POST'])
def comment_list(request, post):
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        
        comments_serializer = CommentSerializer(comments, many=True)
        return JsonResponse(comments_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_data['post']=post 
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
        
