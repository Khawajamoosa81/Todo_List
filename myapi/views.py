from rest_framework import viewsets
from myapi.models import Breed, Dog
from myapi.serializers import BreedSerializer, DogSerializer

# Create your views here.
class BreedView(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    
class DogView(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer