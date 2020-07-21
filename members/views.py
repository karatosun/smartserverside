from .models import Collaborator, Researcher
from rest_framework import generics
from .serializers import CollaboratorSerializers, ResearcherSerializers, CollaboratorListSerializers, ResearcherListSerializers
from django.utils import timezone
from .permissions import IsSuper

# Create your views here.

class CollaboratorListAPIView(generics.ListAPIView):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorListSerializers
    

class ResearcherListAPIView(generics.ListAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherListSerializers

class CollaboratorDetailAPIView(generics.RetrieveAPIView):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializers
    lookup_field = 'pk'
    
class ResearcherDetailAPIView(generics.RetrieveAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializers
    lookup_field = 'pk'

class CollaboratorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializers
    lookup_field = 'pk'
    permission_classes = (IsSuper,)

    def perform_update(self, serializer):
        serializer.save(updated_date = timezone.now())

class ResearcherUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializers
    lookup_field = 'pk'
    permission_classes = (IsSuper,)

    def perform_update(self, serializer):
        serializer.save(updated_date = timezone.now())

class CollaboratorDeleteAPIView(generics.DestroyAPIView):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializers
    lookup_field = 'pk'
    permission_classes = (IsSuper,)

class ResearcherDeleteAPIView(generics.DestroyAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializers
    lookup_field = 'pk'
    permission_classes = (IsSuper,)

class CollaboratorCreateAPIView(generics.CreateAPIView):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializers
    permission_classes = (IsSuper,)

class ResearcherCreateAPIView(generics.CreateAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializers
    permission_classes = (IsSuper,)

