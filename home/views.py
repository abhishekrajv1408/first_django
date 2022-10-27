from django.shortcuts import render
from django.http import HttpResponse
from home.models import Details
from .forms import UserForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    if request.method=='POST':
        form=UserForm()
        form.save()
        if form.is_valid:
            form.save()
        return render(request,'about.html',{'form':form})
    else:
        form=UserForm()
        return render(request,'about.html',{'form':form})