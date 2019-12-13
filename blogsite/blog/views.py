from django.shortcuts import render

# Create your views here.
def index(request):
    """Index Page view"""

    return render(request, "index.html", context={})
