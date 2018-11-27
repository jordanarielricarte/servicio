from .models import Perros
from rest_framework import viewsets
from misperris.serializers import PerroSerializer

class PerroViewSet( viewsets.ModelViewSet ):
    queryset = Perros.objects.all().order_by( 'name' )
    serializer_class = PerroSerializer
