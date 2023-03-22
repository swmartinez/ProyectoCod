from django.db import models

class Smartphone(models.Model): #La clase Smartpohnes hereda todas las propiedasdes de models.Model

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return self.marca + self.modelo + '(' + self.precio + ')'

class Tablet(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return self.marca + self.modelo + '(' + self.precio + ')'

class Tv(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return self.marca + self.modelo + '(' + self.precio + ')'

class Notebook(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return self.marca + self.modelo + '(' + self.precio + ')'

class Contact(models.Model):

    nombre_cliente = models.CharField(max_length=30)
    email = models.EmailField()
    fecha = models.DateField()
    consulta = models.CharField(max_length=60)