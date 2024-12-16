from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Assistance  
from .serializers import AssistanceSerializer  

# ViewSet to list all assistances
class AssistanceViewSet(viewsets.ModelViewSet): 
    queryset = Assistance.objects.all() 
    serializer_class = AssistanceSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['assistance_type', 'date_time', 'extended_assistance']  


