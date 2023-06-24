from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.RoomView.as_view(), name='main'),
]
