from django.shortcuts import render,HttpResponse

# Create your views here.

def app02_index(request):
    return HttpResponse(b'app02_index')