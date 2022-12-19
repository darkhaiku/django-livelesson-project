import json

import pprint

from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)



from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer

from .models import Tag, Startup , NewsLink

# Create your views here.

class TagApiDetail(RetrieveAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # detail need a /slug
    lookup_field = 'slug'



class TagApiList(ListAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# --- Startup ---
class StartupAPIDetail(RetrieveAPIView):

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    # detail need a /slug
    lookup_field = 'slug'

class StartupAPIList(ListAPIView):
    
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
            

# --- it is important & usefull website for Serializer ---
# https://www.cdrf.co/
# --- 

class NewsLinkAPIDetail(RetrieveAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer 

    # we don't use this form
    # lookup_field = 'slug'

    # instead we use this form 
    # ---> 
    def get_object(self):

        startup_slug = self.kwargs.get('startup_slug')
        newslink_slug = self.kwargs.get('newslink_slug')

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug,
        )

        self.check_object_permissions(
            self.request, newslink
        )

        return newslink




class NewsLinkAPIList(ListAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
