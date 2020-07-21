from .models import Entry
from rest_framework import serializers


class EntrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

# class CollaboratorSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = Collaborator
#         fields = '__all__'