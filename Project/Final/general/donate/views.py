from django.shortcuts import render, redirect

from .models import Paydata

from .forms import Paydataform

def index(request):
    paydata= Paydata.objects.all()

    form= Paydataform()

    if request.method =='POST':
        form = Paydataform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'paydata': paydata,'form': form}
    return render(request, 'donate/donate.html', context)
