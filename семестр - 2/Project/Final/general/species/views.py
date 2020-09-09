from django.shortcuts import render
from .models import Animal

def index(request):


    animals=Animal.objects.all()
    context={'animals':animals}

    return render(request, 'species/index.html', context)
