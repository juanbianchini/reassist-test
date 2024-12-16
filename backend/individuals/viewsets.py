from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Individual 
from .serializers import IndividualSerializer  
from assistances.serializers import AssistanceSerializer  


# ViewSet to list all individuals 
class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

# Action to list one individual by their 'pk'
    @action(detail=True, methods=['get'])
    def assistance_history(self, request, pk=None):
        individual = self.get_object()
        assistance_records = individual.assistance_records.all()  
        serializer = AssistanceSerializer(assistance_records, many=True)
        return Response(serializer.data)
