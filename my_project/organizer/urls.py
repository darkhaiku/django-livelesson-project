from django.urls import path

from .views import TagApiDetail, TagApiList


urlpatterns = [
    path('', TagApiList.as_view(), name='api-tag-list' ),

    path('<str:slug>/',
    TagApiDetail.as_view(),
    name='api-tag-detail'
    ),
]

