from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def resources(request):
    return render(request, 'resources.html',)
