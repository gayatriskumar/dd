from django.shortcuts import render
from .models import Contactusform
from django.views.generic import View
from django.http import HttpResponse
from .forms import Contactform
from django.http import JsonResponse
from . import forms

# Create your views here.

def contactusform_view(request):

    if request.method=="POST":
        contactusform=Contactusform()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        description=request.POST.get('description')

        contactusform.name =  name
        contactusform.email = email
        contactusform.phone_no = phone_no
        contactusform.description = description
        contactusform.save()

    form = forms.Contactform()
    return render(request,'contactusform/form.html', {'form': form})


def database_view(request):
    form = Contactusform.objects.all()
    return render(request,'contactusform/database.html', {'form': form})