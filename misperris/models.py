from django.db import models

class Perros( models.Model ):
    id = models.AutoField( primary_key = True )
    name = models.CharField( max_length = 255 )
    description = models.TextField( default= '' )
    status = models.CharField( max_length = 255, default = 'Disponible')
    imageUrl = models.CharField( max_length = 255, default = '' )

    def __str__( self ):
        return self.name