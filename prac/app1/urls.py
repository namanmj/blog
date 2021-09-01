from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.blog_list,name='blog_list'),
    path('detail/<int:pk>/',views.detail_blog,name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:pk>', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'),
    path('signup',views.register,name='register'),
    path('login',views.login_request,name='login'),
     path('logout',views.logout_request,name='logout'),
]