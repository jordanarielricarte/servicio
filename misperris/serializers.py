from .models import Perros
from rest_framework import serializers

class PerroSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Perros
        fields = ( 'id', 'name', 'description','status', 'imageUrl' )