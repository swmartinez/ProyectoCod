from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *

def inicio(request):
    return render(request, 'AppUno/inicio.html')

def smartphone(request):
    if request.method == 'POST':
        formulario = SmartphoneForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            smartphones = Smartphone(marca=informacion['marca'], 
                                     modelo=informacion['modelo'], 
                                     fecha_de_entrega=informacion['fecha_de_entrega'], 
                                     precio=informacion['precio'])
            smartphones.save()
            return redirect('inicio')
    else:
        formulario = SmartphoneForm()
        
    return render(request, 'AppUno/smartphones.html',{'form_smartphones': formulario})


def tablet(request):
    if request.method == 'POST':
        formulario = TabletForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            tablets = Tablet(marca=informacion['marca'], 
                             modelo=informacion['modelo'], 
                             fecha_de_entrega=informacion['fecha_de_entrega'], 
                             precio = informacion['precio'])
            tablets.save()
            return redirect('inicio')
    else:
        formulario = TabletForm()
        
    return render(request, 'AppUno/tablets.html',{'form_tablets': formulario})   


def tv(request):
    if request.method == 'POST':
        formulario = TvForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            tvs = Tv(marca=informacion['marca'], 
                     modelo=informacion['modelo'], 
                     fecha_de_entrega=informacion['fecha_de_entrega'], 
                     precio = informacion['precio'])
            tvs.save()
            return redirect('inicio')
    else:
        formulario = TvForm()
        
    return render(request, 'AppUno/tvs.html',{'form_tvs': formulario})


def notebook(request):
    if request.method == 'POST':
        formulario = NotebookForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            notebook = Notebook(marca=informacion['marca'], 
                                modelo=informacion['modelo'], 
                                fecha_de_entrega=informacion['fecha_de_entrega'], 
                                precio = informacion['precio'])
            notebook.save()
            return redirect('inicio')  
    else:
        formulario = NotebookForm()
        
    return render(request, 'AppUno/notebooks.html',{'form_notebook': formulario})


def contact(request):
    if request.method == 'POST':
        formulario = ContactForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            contact = Contact(nombre_cliente=informacion['nombre_cliente'], 
                              email=informacion['email'], 
                              fecha=informacion['fecha'], 
                              consulta = informacion['consulta'])
            contact.save()
            return redirect('inicio') 
    else:
        formulario = ContactForm()
        
    return render(request, 'AppUno/contact-forms.html', {'form_contact': formulario})


def buscar_producto(request):
    return render(request, 'AppUno/busqueda-producto.html')


def buscar(request):
    if request.GET["marca"]:
        mi_marca = request.GET["marca"]
        resultado =  Notebook.objects.filter(marca__icontains=mi_marca)

        return render(request, 'AppUno/resultados-busqueda.html', {"notebooks": resultado, "marca": mi_marca})
    else:
        respuesta = 'No se econtraron productos con la clave especificada.'

    return HttpResponse(respuesta)