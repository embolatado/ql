from django.shortcuts import render

# Create your views here.

def inicio(request):
    titulo = "Título dinámico"
    return render(request, 'blog/index.html', {"titulo": titulo})


def about(request):
    return render(request, 'blog/about.html')
