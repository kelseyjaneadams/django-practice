from django.shortcuts import render

# Create your views here.

# When you call this function, it’ll render an HTML file named home.html. 
def home(request):
    return render(request, "pages/home.html", {})