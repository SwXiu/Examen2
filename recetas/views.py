from django.shortcuts import render
import requests
from django.shortcuts import redirect
# Create your views here.
def ir(request):
    response = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
    data = response.json()
    categorias = data['meals']
       
    if categorias:
        primeraCategoria = categorias[0]['strCategory']
        return redirect('recetas:obtenerCategoria', categoria=primeraCategoria)
    else:
        return redirect('recetas:obtenerRecetas')

def getRecetas(request, categoria):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={categoria}"
    
    try:
        response = requests.get(url)
        if response.ok:
            categorias = response.json()
            recetas = categorias['meals']
            print(categorias['meals'])
        else:
            print("Error al obtener los datos")

        return render(request, "index.html", {
            'categoria': categoria,
            'recetas': recetas
        })
    except requests.exceptions.RequestException as e:
        return print(f"Error de conexión: {str(e)}", status=500)
    
from django.shortcuts import render
import requests

def getCategoria(request, categoria):
    try:
        response = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={categoria}')
        data = response.json()
        recetas = data.get('meals', [])
    except Exception as e:
        print(f"Error obteniendo recetas: {e}")
        recetas = []
    
    try:
        response_categorias = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
        data_categorias = response_categorias.json()
        categorias = data_categorias.get('meals', [])
    except Exception as e:
        print(f"Error obteniendo categorías: {e}")
        categorias = []
    
    return render(request, 'index.html', {
        'categoria_actual': categoria,
        'categorias': categorias,
        'recetas': recetas
    })