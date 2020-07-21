from .models import Entry
from rest_framework import generics
from .serializers import EntrySerializers
# from django.utils import timezone
from .permissions import IsSuper, IsOwner
from rest_framework.parsers import MultiPartParser, FormParser

class EntryListAPIView(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializers
    # permission_classes = (IsSuper,)
    
class EntryDetailAPIView(generics.RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializers
    # permission_classes = (IsSuper,)
    lookup_field = 'pk'

class EntryDeleteAPIView(generics.DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializers
    # permission_classes = (IsSuper,)
    lookup_field = 'pk'

class EntryCreateAPIView(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializers
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = (IsOwner,)

    # def perform_create(self, serializer):
    #     serializer.save(username=self.request.user.username)

class EntryUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializers
    # permission_classes = (IsOwner,)
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'pk'

    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)
