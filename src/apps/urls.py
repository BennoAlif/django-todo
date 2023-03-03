from django.urls import path, include
from rest_framework.routers import DefaultRouter
import apps.views as views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
