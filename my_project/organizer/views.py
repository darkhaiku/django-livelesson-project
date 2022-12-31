import json

import pprint

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)




from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer

from .models import Tag, Startup , NewsLink

# Create your views here.

class TagList(ListView):

    queryset = Tag.objects.all()
    template_name = "tag/list.html"

class TagDetail(DetailView):

    queryset = Tag.objects.all()
    template_name = "tag/detail.html"


class TagApiDetail(RetrieveAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # detail need a /slug
    lookup_field = 'slug'

    def patch(self, request, slug):
        """ update existing Tag with patch """
        """ using patch method instead of put method """
        tag = self.get_object()
        s_tag = self.serializer_class(
            tag, 
            data=request.data,
            context = {'request': request},
        )
        if s_tag.is_valid():
            s_tag.save()
            return Response(s_tag.data, status=HTTP_200_OK)
        return Response(
            s_tag.errors, status=HTTP_400_BAD_REQUEST
        )



class TagApiList(ListCreateAPIView):

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
