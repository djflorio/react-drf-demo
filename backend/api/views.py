from api.models import Painting, Artist
from api.serializers import PaintingSerializer, ArtistSerializer
from rest_framework import generics
from rest_framework import permissions

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PaintingList(generics.ListCreateAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PaintingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)