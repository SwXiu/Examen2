from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('recetas/', include('recetas.urls', namespace='recetas')),
]
