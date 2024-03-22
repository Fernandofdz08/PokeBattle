from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def prueba(request):
    a = 5
    b = 3
    c = a + b
    print(c)
    return HttpResponse(f"La suma de {a} + {b} es igual a {c}")