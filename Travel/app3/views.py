from django.shortcuts import render
from .models import Place
from .models import People
# Create your views here.
from django.http import HttpResponse
def demo(request):
    obj=Place.objects.all()
    obj2=People.objects.all()
    return render(request, 'index.html',{'result': obj,'result2': obj2})

