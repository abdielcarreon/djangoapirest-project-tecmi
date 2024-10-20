from rest_framework import viewsets
from .models import Fields
from .serializer import FieldSerializer

class FieldsViewSet(viewsets.ModelViewSet):
    queryset = Fields.objects.all()
    serializer_class = FieldSerializer