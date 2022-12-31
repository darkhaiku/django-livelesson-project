from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from .serializers import TrackSerializer, AlbumSerializer

from .models import Track, Album

# Create your views here.

class TrackApiList(ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class AlbumApiList(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer