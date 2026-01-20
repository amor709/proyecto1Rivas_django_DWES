from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'core/inicio.html')

@login_required
def privado(request):
    return render(request, 'core/privado.html')

# def logout(request):
#     if request.method == 'POST':
        
