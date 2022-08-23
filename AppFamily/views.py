from cgitb import text
import email
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import familia

def familiares(request):
    Familiar = familia(nombre = "yareli",apellido="Antonio",apePaterno="Flores",fechaNacimiento="14/01/1995",telefono=2253698789,email="yali123@gmail.com")
    Familiar.save()
    texto1=f"Familiar creado: {Familiar.nombre} {Familiar.apePaterno} {Familiar.apellido} con fecha de Nacimiento: {Familiar.fechaNacimiento} telefono: {Familiar.telefono} email: {Familiar.email} \n "
    Familiar1 = familia(nombre = "yareli",apellido="Antonio",apePaterno="Flores",fechaNacimiento="14/01/1995",telefono=2253698789,email="yali123@gmail.com")
    Familiar1.save()
    texto2=f"Familiar creado: {Familiar1.nombre} {Familiar1.apePaterno} {Familiar1.apellido} con fecha de Nacimiento: {Familiar1.fechaNacimiento} telefono: {Familiar1.telefono} email: {Familiar1.email} \n "
    Familiar2 = familia(nombre = "yareli",apellido="Antonio",apePaterno="Flores",fechaNacimiento="14/01/1995",telefono=2253698789,email="yali123@gmail.com")
    Familiar2.save()
    texto3=f"Familiar creado: {Familiar2.nombre} {Familiar2.apePaterno} {Familiar2.apellido} con fecha de Nacimiento: {Familiar2.fechaNacimiento} telefono: {Familiar2.telefono} email: {Familiar2.email} \n "
    texto=texto1+texto2+texto3
    return HttpResponse(texto)




