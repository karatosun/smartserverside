from django.urls import path
#from django.views.decorators.cache import cache_page

from user import views

app_name = "user"

urlpatterns = [
    
    path('update/<pk>', views.UpdatePassword.as_view(), name='user-update'),
    path('register/', views.UserRegisterAPIView.as_view(), name='user-create'),
    ]


