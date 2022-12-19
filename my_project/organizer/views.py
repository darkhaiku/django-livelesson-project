import json

import pprint

from django.shortcuts import render



from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)



from .serializers import TagSerializer, StartupSerializer

from .models import Tag, Startup

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
