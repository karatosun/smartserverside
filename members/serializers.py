from .models import Collaborator, Researcher
from rest_framework import serializers

class CollaboratorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'
    
        

class CollaboratorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Collaborator
        fields = '__all__'

class ResearcherListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Researcher
        fields = '__all__'

class ResearcherSerializers(serializers.ModelSerializer):
        
    class Meta:
        model = Researcher
        fields = '__all__'