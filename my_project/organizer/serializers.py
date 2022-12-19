
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedRelatedField,
)

from rest_framework.reverse import reverse

from .models import NewsLink, Startup, Tag

class TagSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug',
                'view_name':'api-tag-detail',

            }
        }

class StartupSerializer(HyperlinkedModelSerializer):
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
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug',
                'view_name': 'api-startup-detail'
            }
        }

class NewsLinkSerializer(ModelSerializer):
    """Serialize NewsLink data"""

    url = SerializerMethodField()
    startup = HyperlinkedRelatedField(
        queryset=Startup.objects.all(),
        lookup_field="slug",
        view_name="api-startup-detail",
    )

    class Meta:
        model = NewsLink
        exclude = ("id",)

    def get_url(self, newslink):
        """Build full URL for NewsLink API detail"""
        return reverse(
            "api-newslink-detail",
            kwargs=dict(
                startup_slug=newslink.startup.slug,
                newslink_slug=newslink.slug,
            ),
            request=self.context["request"],
        )