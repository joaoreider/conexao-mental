from django.http import HttpResponse


from django.shortcuts import render

def avaliacao(request):
    return render(request, 'avaliacao.html')