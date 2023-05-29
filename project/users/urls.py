from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'create', UserCreateViewSet, basename='create')
router.register(r'login', UserLoginViewSet, basename='login')

app_name='users'
urlpatterns = [
    # path('', include(router.urls)),
    path('', hello),
]