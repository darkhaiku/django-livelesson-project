from django.urls import path

from .views import (
    TrackApiList,
    AlbumApiList,
)

urlpatterns = [
    path('album/', AlbumApiList.as_view(), name='api-album-list'),

    path('track/',TrackApiList.as_view(), name='api-track-list'),
]