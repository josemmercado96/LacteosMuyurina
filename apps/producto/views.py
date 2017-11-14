from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RefrigeracionForm, TipoProductoForm, ProductoForm
from .models import Refrigeracion, TipoProducto, Producto
# Create your views here.

def crearRefrigeracion(request):
    if request.method == 'POST':
        form = RefrigeracionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productos:listaRefrigeracion')
    else:
        form = RefrigeracionForm()
    
    return render(request, 'producto/crear_refrigeracion.html',{'form':form})
            
def listaRefrigeracion(request):
    refrigeracion = Refrigeracion.objects.all()
    context = {'refrigeraciones':refrigeracion}
    return render(request,'producto/lista_refrigeracion.html',context)

def crearTipo(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productos:listaTipos')
    else:
        form = TipoProductoForm()

    return render(request,'producto/crear_tipo.html',{'form':form})

def listaTipos(request):
    tipo = TipoProducto.objects.all()
    context = {'tipos':tipo}
    return render(request,'producto/lista_tipos.html',context)

def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productos:listaProductos')
    else:
        form = ProductoForm()

    return render(request,'producto/crear_producto.html',{'form':form})

def listaProductos(request):
    producto = Producto.objects.all()
    context = {'productos':producto}
    return render(request,'producto/lista_productos.html',context)