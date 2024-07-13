from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('posts/',views.posts, name= 'posts'),
    path('posts/<int:post_id>/',views.post_detail,name='post_detail'),
    path('categories/',views.categories, name='categories'),
    path('comments/',views.comments_fetch,name='comments'),

]
