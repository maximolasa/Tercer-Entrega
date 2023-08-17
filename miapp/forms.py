from django import forms
from .models import Categoria, Producto, Cliente, Review  # Asegúrate de importar Review

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'categoria')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'email')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('juego', 'resena', 'calificacion')