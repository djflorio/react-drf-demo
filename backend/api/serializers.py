from rest_framework import serializers
from api.models import Painting, Artist



class ArtistSerializer(serializers.ModelSerializer):
    paintings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  
    class Meta:
        model = Artist
        fields = ('id', 'name', 'paintings', 'biography', 'image', 'source')
        
class PaintingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Painting
        fields = (
          'id', 'name', 'artist', 'description',
          'retail_price', 'price', 'image', 'source')