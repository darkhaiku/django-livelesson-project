
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
)

from .models import NewsLink, Startup, Tag

class TagSerializer(ModelSerializer):
    
    url = HyperlinkedIdentityField(
        lookup_field="slug", view_name="api-tag-detail",
    )

    class Meta:
        model = Tag
        fields = "__all__"

class StartupSerializer(ModelSerializer):
    # --> remove all of them 

    # id = IntegerField(read_only=True)
    # name = CharField(max_length=31)
    # slug = SlugField(max_length=31)
    # description = CharField()
    # founded_date = DateField()
    # contact = EmailField()
    # website = URLField(max_length=225)

    # <-- remove all of them 
    tags = TagSerializer(many=True)

    class Meta:
        model = Startup
        fields = "__all__"

class NewsLinkSerializer(ModelSerializer):

    startup = StartupSerializer()

    class Meta:
        model = NewsLink
        fields = "__all__"
