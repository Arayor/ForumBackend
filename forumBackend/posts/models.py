from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=70, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

class Comment(models.Model):
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)