from django.shortcuts import render
from cricketer_profiler_app.models import *

# Create your views here.
def summarize(text):
    wordList = text.split(" ")[0:18]
    newSummary = " ".join(wordList)
    return newSummary
    
def index(request):
    return render(request, 'index.html')

def cricketers(request, role=""):
    allCricketers = Cricketer.objects.all()
    if 'search' in request.GET:
        searchWords = request.GET['search'].split(" ")
        cricketers = []
        for search in searchWords:
            cricketers.extend(allCricketers.filter(name__icontains=search))
        allCricketers = cricketers
    elif role == "coach":
        coaches = Coach.objects.all()
        cricketers = []
        for coach in coaches:
            cricketers.append(coach.cricketer)
        allCricketers = cricketers
    elif role in ["batsman", "bowler", "allrounder"]:
        allCricketers = allCricketers.filter(player_role__icontains=role)
    for cricketer in allCricketers:
        cricketer.description = summarize(cricketer.description)
    return render(request, 'cricketers.html', {'cricketers': allCricketers})

def cricketer(request, id):
    cricketer = Cricketer.objects.get(id=id)
    return render(request, 'cricketer.html', {'cricketer': cricketer})

def teams(request):
    allTeams = Team.objects.all()
    return render(request, 'teams.html', {'teams': allTeams})

def matches(request):
    return render(request, 'matches.html')

def liveMatches(request):
    return render(request, 'livematches.html')