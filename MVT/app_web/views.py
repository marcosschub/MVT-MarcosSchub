from django.shortcuts import render

def listar_familiares(request):
    context={}
    context["familiares"]=Familiar.objects.all()
    return render(request,"app_web/index.html",context)
