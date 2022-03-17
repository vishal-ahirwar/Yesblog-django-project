from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, "base/frontpage.html")

def AboutPage(request):
    return render(request, "base/about.html")