from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def join(request):
    return render(request, 'join.html',)
