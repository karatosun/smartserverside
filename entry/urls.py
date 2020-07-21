from django.urls import path
#from django.views.decorators.cache import cache_page

from entry.views import EntryListAPIView, EntryDetailAPIView, EntryUpdateAPIView, EntryDeleteAPIView, EntryCreateAPIView

app_name = "entry"

urlpatterns = [
    path('', EntryListAPIView.as_view(), name='entries'),
    path('<pk>', EntryDetailAPIView.as_view(), name='entry-detail'),
    path('update/<pk>', EntryUpdateAPIView.as_view(), name='entry-update'),    
    path('delete/<pk>', EntryDeleteAPIView.as_view(), name='entry-delete'),
    path('create/', EntryCreateAPIView.as_view(), name='entry-create'),
    ]


