from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostsViewSet, CommentsViewSet, GroupsViewSet, FollowsViewSet

v1_router = DefaultRouter()

v1_router.register(r'^posts', PostsViewSet, basename='api_posts')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentsViewSet, basename='api_comments')

v1_router.register(r'^group', GroupsViewSet, basename='api_groups')
v1_router.register(r'^follow', FollowsViewSet, basename='api_followers')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
