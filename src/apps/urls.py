from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import apps.views as views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    # obtain JWT token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # refresh JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
