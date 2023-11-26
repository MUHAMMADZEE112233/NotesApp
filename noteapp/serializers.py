from rest_framework import serializers
from .models import Notess

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notess
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
