from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'front/landing.html')

def dasbor(request):
    return render(request, 'front/dasbor.html')

def akun(request):
    return render(request, 'akun/index.html')

def edit(request):
    return render(request, 'akun/editakun.html')
