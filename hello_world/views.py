from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)







    
