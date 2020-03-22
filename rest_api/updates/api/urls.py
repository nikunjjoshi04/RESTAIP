from django.urls import path
from .views import UpdateModelDetailAPIView, UpdateModelListAPIView

urlpatterns = [
    path('', UpdateModelListAPIView.as_view(), name='api_update_list'),
    path('<int:id>/', UpdateModelDetailAPIView.as_view(), name='api_update_list'),
]
