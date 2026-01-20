from django.contrib import admin
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

from .models import Question, Choice

# def index(request):
#     if request.user.has_perm('polls.view_question'):
#         return HttpResponse("Acceso permitido: You are at the polls index.")
#     return HttpResponse("Acceso denegado")




# @permission_required(perm:"polls.add_question", raise_exception=True)
# def index(reqyest):
#     return HttpResponse("Acceso permitido: Hello, world. You re at the polls index")


# Register your models here.
