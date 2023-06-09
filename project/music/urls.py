from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'music', MusicViewSet, basename='music')
router.register(r'playmusic', UserMusicViewSet, basename='usermusic')

app_name='music'
urlpatterns = [
    path('', include(router.urls)),
]