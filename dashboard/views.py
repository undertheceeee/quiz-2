from django.shortcuts import render
from portfolio.models import Portfolio
from django.contrib.auth.models import User

def list_view(request):
    users = User.objects.filter(portfolio__isnull=False)
    return render(request, 'dashboard/list.html', {'users': users})

# Create your views here.
