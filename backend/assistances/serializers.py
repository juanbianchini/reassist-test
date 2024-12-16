from rest_framework import serializers
from .models import Assistance

# Serializer Individual
class AssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = '__all__'
