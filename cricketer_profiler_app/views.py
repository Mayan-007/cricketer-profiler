from django.shortcuts import render
from cricketer_profiler_app.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def allCricketers(request):
    cricketers = Cricketer.objects.all()
    return render(request, 'all_cricketers.html', {'cricketers': cricketers})

def allCoaches(request):
    return render(request, 'all_coaches.html')

def allTeams(request):
    return render(request, 'all_teams.html')

def allMatches(request):
    return render(request, 'all_matches.html')