from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context={'a': 'ZIKRA'}
    return render(request,'index.html', context)


def melanoma(request):
    return render(request,'melanoma.html')