from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ClienteForm, ReviewForm
from .models import Producto, Review

def index(request):
    return render(request, 'index.html')

def insertar_datos(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        producto_form = ProductoForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if categoria_form.is_valid() and producto_form.is_valid() and cliente_form.is_valid():
            categoria = categoria_form.save()
            producto = producto_form.save(commit=False)
            producto.categoria = categoria
            producto.save()
            cliente_form.save()

    else:
        categoria_form = CategoriaForm()
        producto_form = ProductoForm()
        cliente_form = ClienteForm()

    return render(request, 'insertar_datos.html', {
        'categoria_form': categoria_form,
        'producto_form': producto_form,
        'cliente_form': cliente_form,
    })

def buscar(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        resultados = Producto.objects.filter(nombre__icontains=query)
    else:
        resultados = []

    return render(request, 'buscar.html', {'resultados': resultados})


