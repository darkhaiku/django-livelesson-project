from rest_framework import serializers

from .models import Album , Track

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.RelatedField(many=True, read_only=True)
    
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')

class TrackSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Track
        fields = ('album', 'order', 'title', 'duration' )

        