from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tools(request):
    return render(request, 'tools.html',)
