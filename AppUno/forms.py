from django import forms

class ContactForm(forms.Form):

    nombre_cliente = forms.CharField(max_length=30)
    email = forms.EmailField()
    fecha = forms.DateField()
    consulta = forms.CharField(max_length=60)

class TabletForm(forms.Form):

    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    fecha_de_entrega = forms.DateField()
    precio = forms.IntegerField()

class NotebookForm(forms.Form):

    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    fecha_de_entrega = forms.DateField()
    precio = forms.IntegerField()

class TvForm(forms.Form):

    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    fecha_de_entrega = forms.DateField()
    precio = forms.IntegerField()

class SmartphoneForm(forms.Form):

    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    fecha_de_entrega = forms.DateField()
    precio = forms.IntegerField()