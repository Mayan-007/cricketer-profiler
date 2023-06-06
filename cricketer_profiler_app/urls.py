from django.urls import path
from cricketer_profiler_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('cricketers/', allCricketers, name='all_cricketers'),
    path('coaches/', allCoaches, name='all_coaches'),
    path('teams/', allTeams, name='all_teams'),
    path('matches/', allMatches, name='all_matches'),
]