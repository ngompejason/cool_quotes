from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def homepage(request):
    quotes = Quote.objects.all()
    context = {'quotes':quotes}
    
    template = "quotes/homepage.html"
    return render(request, template, context)

@login_required(login_url="/accounts/login/")
def ofatd(request):
    template = "quotes/ofatd.html"
    return render(request, template)