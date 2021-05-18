from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('redoc/', TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/', include('api.urls')),
]
