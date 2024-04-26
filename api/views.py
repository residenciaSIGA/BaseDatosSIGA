from rest_framework import viewsets
from .serializer import TipoDocSerializer
from .models import TipoDoc

#create your views here

class TipoDocViewSet(viewsets.ModelViewSet):
    queryset = TipoDoc.objects.all()
    serializer_class = TipoDocSerializer