from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    template = "quotes/homepage.html"
    return render(request, template)

@login_required(login_url="/accounts/login/")
def ofatd(request):
    template = "quotes/ofatd.html"
    return render(request, template)