from rest_framework import serializers
from .models import Assistance

# Serializer Assistance
class AssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = '__all__'
