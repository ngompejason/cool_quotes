from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def homepage(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 20)
    
    page_number = request.GET.get('page', 1)
    
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        }
    
    template = "quotes/homepage.html"
    return render(request, template, context)

#==========================================================
#------------------------Quote View------------------------
#==========================================================
def all_quotes(request):
    quotes = Quote.objects.filter()
    paginator = Paginator(quotes, 20)
    
    page_number = request.GET.get('page', 1)
    
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        }
    
    template = "quotes/all_quotes.html"
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
    

@login_required(login_url="/accounts/login/")
def edit_quote(request, quote_id):
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=quote_id)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = QuoteForm(instance=quote_id)
    
    template = "quotes/create_quote.html"
    return render(request, template, {"form":form})

@login_required(login_url="/accounts/login/")
def delete_quote(request, quote_id):
    if request.method == 'POST':
        quote = get_object_or_404(Quote, id=quote_id)
        quote.delete()
        messages.success(request, 'Quote deleted successfully!')
        return redirect('homepage')  # Replace with your list view name
    return redirect('homepage')

#==========================================================
#----------------------Vote View---------------------------
#==========================================================

def vote_quote(request, quote_id, vote_type):
    
    quote = get_object_or_404(Quote, id=quote_id)
    vote_type = int(vote_type)
    existing_vote = Vote.objects.filter(quote=quote, user=request.user).first()
    
    if existing_vote:
        if existing_vote.vote_type == vote_type:
            existing_vote.delete()
            messages.success(request, "You have remove your vote.")
        else:
            existing_vote.vote_type = vote_type
            existing_vote.save()
            messages.success(request, "Your vote has been updated.")
    else:
        Vote.objects.create(
            quote=quote,
            user=request.user,
            vote_type = vote_type
        )
        messages.success(request, "You just voted.")
        
    
    # Redirect back to the referring page or a fallback if unavailable
    next_url = request.GET.get('next', request.META.get('HTTP_REFERER', '/'))
    return redirect(next_url)

#==========================================================
#----------------------Report View-------------------------
#==========================================================

@login_required(login_url="/accounts/login/")
def create_report(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.quote = quote
            report.save()
            return redirect(f"/quote/{quote_id}")
    else:
        form = ReportForm()
    template = "reports/create_report.html"
    return render(request, template, {"form":form})


@login_required(login_url="/accounts/login/")
def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    quotes = Quote.objects.filter(user=user).prefetch_related('reports')
    context = {
        "user":user,
        "quotes":quotes
    }
    template = "accounts/user_profile.html"
    return render(request, template, context)