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

def replaceEmptyWithDash(stat):
    for each in stat:
        for key, value in each.__dict__.items():
            if value == -1:
                each.__dict__[key] = "-"
    return stat

def cricketer(request, id):
    cricketer = Cricketer.objects.get(id=id)
    batstats = replaceEmptyWithDash(BattingCareer.objects.filter(cricketer=cricketer).order_by('-match_format'))
    bowlstats = replaceEmptyWithDash(BowlingCareer.objects.filter(cricketer=cricketer).order_by('-match_format'))
    fieldstats = replaceEmptyWithDash(FieldingCareer.objects.filter(cricketer=cricketer).order_by('-match_format'))
    return render(request, 'cricketer.html', {'cricketer': cricketer, 'batstats': batstats, 'bowlstats': bowlstats, 'fieldstats': fieldstats})

def typeId(type):
    match_format = MatchFormat.objects.get(match_format__iexact=type)
    return match_format.id

def teams(request, type=""):
    allTeams = Team.objects.all()
    if 'search' in request.GET:
        searchWords = request.GET['search'].split(" ")
        teams = []
        for search in searchWords:
            teams.extend(allTeams.filter(team_name__icontains=search))
        allTeams = teams
    elif type in ["T20I", "ODI", "Test", "IPL"]:
        allTeams = allTeams.filter(team_format=typeId(str(type)))
    for team in allTeams:
        team.description = summarize(team.description)
    return render(request, 'teams.html', {'teams': allTeams})

def team(request, id):
    team = Team.objects.get(id=id)
    batsmen = CricketerTeam.objects.filter(team=team, cricketer__player_role__icontains="batsman")
    allrounders = CricketerTeam.objects.filter(team=team, cricketer__player_role__icontains="allrounder")
    wicket_keepers = CricketerTeam.objects.filter(team=team, cricketer__player_role__icontains="wicketkeeper")
    bowlers = CricketerTeam.objects.filter(team=team, cricketer__player_role__icontains="bowler")
    return render(request, 'team.html', {'team': team, 'batsmen': batsmen, 'allrounders': allrounders, 'wicket_keepers': wicket_keepers, 'bowlers': bowlers})

def matches(request):
    matches = Match.objects.all()
    return render(request, 'matches.html', {'matches': matches})

def liveMatches(request):
    return render(request, 'livematches.html')