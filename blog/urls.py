from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentListCreateAPIView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='post-comments'),
]
