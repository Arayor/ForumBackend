from django.conf.urls import url 
from posts import views 
from django.urls import path
 
urlpatterns = [ 
    path('api/posts/', views.post_list),
    path('api/posts/<int:id>/', views.post_detail),
    path('api/posts/<int:post>/comments', views.comment_list),
]