from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RefrigeracionForm, TipoProductoForm, ProductoForm, LoteForm
from .models import Refrigeracion, TipoProducto, Producto, LoteProduccion
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
    tipo = TipoProducto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productos:listaProductos')
    else:
        form = ProductoForm()

    return render(request,'producto/crear_producto.html',{'form':form,'tipos':tipo})

def listaProductos(request):
    producto = Producto.objects.all()
    context = {'productos':producto}
    return render(request,'producto/lista_productos.html',context)

def crearLote(request):
    if request.method == 'POST':
        form = LoteForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data.get('producto')
            c = form.cleaned_data.get('cantidad')
            prod = get_object_or_404(Producto, nombre=p)
            prod.stock += c 
            prod.save()
            form.save()
            return redirect('productos:listaLote')
    else:
        form = LoteForm()

    return render(request,'producto/crear_lote.html',{'form':form})

def  listaLote(request):
    lote = LoteProduccion.objects.all();
    context = {'lotes':lote}
    return render(request, 'producto/lista_lote.html', context)