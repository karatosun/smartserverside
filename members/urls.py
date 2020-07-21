from django.urls import path
#from django.views.decorators.cache import cache_page

from members.views import (CollaboratorListAPIView, ResearcherListAPIView,
                           ResearcherDetailAPIView, CollaboratorDetailAPIView,
                           ResearcherUpdateAPIView, CollaboratorUpdateAPIView,
                           CollaboratorDeleteAPIView, ResearcherDeleteAPIView,
                           ResearcherCreateAPIView, CollaboratorCreateAPIView)

app_name = "members"

urlpatterns = [
    path('collaborators', CollaboratorListAPIView.as_view(), name='collaborators'),
    path('researchers', ResearcherListAPIView.as_view(), name='researchers'),
    path('researchers/<pk>', ResearcherDetailAPIView.as_view(), name='detailres'),
    path('collaborators/<pk>', CollaboratorDetailAPIView.as_view(), name='cdetailcol'),
    path('researchers/update/<pk>', ResearcherUpdateAPIView.as_view(), name='updateres'),
    path('collaborators/update/<pk>', CollaboratorUpdateAPIView.as_view(), name='updatecol'),
    path('researchers/delete/<pk>', ResearcherDeleteAPIView.as_view(), name='deleteres'),
    path('collaborators/delete/<pk>', CollaboratorDeleteAPIView.as_view(), name='deletecol'),
    path('researchers/create/', ResearcherCreateAPIView.as_view(), name='createres'),
    path('collaborators/create/', CollaboratorCreateAPIView.as_view(), name='createcol')
]


