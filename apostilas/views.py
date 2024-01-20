from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def adicionar_apostilas(request):
    if request.method == "GET":
        return render(request, 'adicionar_apostilas.html')
    elif request.method == "POST":
        return HttpResponse('teste')