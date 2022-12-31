from django.urls import path

from .views import (
    TagApiDetail,
    TagApiList,
    StartupAPIDetail,
    StartupAPIList,
    NewsLinkAPIList,
    NewsLinkAPIDetail,
    )


from .views import TagDetail, TagList

urlpatterns = [
    path('tag/', TagApiList.as_view(), name='api-tag-list' ),

    path('tag/<str:slug>/',
    TagApiDetail.as_view(),
    name='api-tag-detail'
    ),

    path("tag/", TagList.as_view(), name="tag_list"),
    path("tag/<str:slug>/", TagDetail.as_view(), name="tag_detail"),

    path('startup/', StartupAPIList.as_view(), name='api-startup-list'),

    path('startup/<str:slug>/',
    StartupAPIDetail.as_view(),
    name='api-startup-detail'),

    path('newslink/', NewsLinkAPIList.as_view(), name='api-newslink-list'),

    path('newslink/<str:startup_slug>/<str:newslink_slug>/',
    NewsLinkAPIDetail.as_view(),
    name='api-newslink-detail'
    )

]

