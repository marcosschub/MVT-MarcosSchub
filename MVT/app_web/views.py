from django.shortcuts import render
from app_web.models import Familiar

def listar_familiares(request):
    context={}
    context["familiares"]=Familiar.objects.all()
    return render(request,"app_web/index.html",context)
