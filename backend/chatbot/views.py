from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IndividualSerializer, AssistanceSerializer

@api_view(['POST'])
def chatbot_individuals(request):
    serializer = IndividualSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success', 'data': serializer.data}, status=201)
    return Response({'status': 'error', 'errors': serializer.errors}, status=400)



@api_view(['POST'])
def chatbot_assistances(request):
    serializer = AssistanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success', 'data': serializer.data}, status=201)
    return Response({'status': 'error', 'errors': serializer.errors}, status=400)
