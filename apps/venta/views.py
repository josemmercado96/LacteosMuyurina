from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClienteForm
from .models import Cliente

# Create your views here.

def index(request):
	return render(request, 'venta/index.html')

def crearCliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('ventas:index')
	else:
		form = ClienteForm()

	return render(request,'venta/crear_cliente.html',{'form':form})

def listaCliente(request):
	cliente = Cliente.objects.all()
	context = {'clientes':cliente}
	return render(request,'venta/lista_clientes.html',context)