from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='booking'),
    path('form/', views.booking, name='booking'),
    path('', views.PostDetail, name='post_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]