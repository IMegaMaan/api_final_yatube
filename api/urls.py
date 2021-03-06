from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from .views import PostsViewSet, CommentsViewSet, GroupsViewSet, FollowsViewSet

v1_router = DefaultRouter()

v1_router.register(r'^posts', PostsViewSet, basename='api_posts')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentsViewSet, basename='api_comments')

v1_router.register(r'^group', GroupsViewSet, basename='api_groups')
v1_router.register(r'^follow', FollowsViewSet, basename='api_followers')

urlpatterns = [
    path('v1/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/', include(v1_router.urls)),
]
