from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    if request.is_ajax():
        if request.method == 'POST':
            v1 = request.POST.get('i1')
            v2 = request.POST.get('i2')
            v3 = int(v1) + int(v2)

            return HttpResponse(v3)

    return render(request,'index.html')