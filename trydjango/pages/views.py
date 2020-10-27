from django.shortcuts import render

# Create your views here.
def hjem_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Velkommen til Lindesnes håndbak klubb sin hjemmeside</h1>") 
    return render(request, "hjem.html", {})

def members_view(request, *args, **kwargs):
    return render(request, "medlemmer.html", {})

def kontakt_oss_view(request, *args, **kwargs):
    return render(request, "kontakt_oss.html", {})

def om_oss_view(request, *args, **kwargs):
    return render(request, "om_oss.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def logout_view(request, *args, **kwargs):
    return render(request, "logout.html", {})