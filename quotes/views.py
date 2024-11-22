from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import QuoteForm

# Create your views here.

def homepage(request):
    quotes = Quote.objects.all()
    context = {'quotes':quotes}
    
    template = "quotes/homepage.html"
    return render(request, template, context)



def quote_detail(request, quote_id):
    quote = get_object_or_404(Quote, id = quote_id)
    context = {
        "quote":quote
    }
    template = "quotes/quote_detail.html"
    return render(request, template, context)


@login_required(login_url="/accounts/login/")
def create_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect("/")
    else:
        form = QuoteForm()
    
    template = "quotes/create_quote.html"
    return render(request, template, {"form":form})
    

