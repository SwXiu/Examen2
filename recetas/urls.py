from django.urls import path
from . import views

app_name = "recetas"

urlpatterns = [
    path('', views.ir, name="obtenerRecetas"),
    path('<str:categoria>/', views.getCategoria, name="obtenerCategoria"),
]
