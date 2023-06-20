from django.urls import path
from cricketer_profiler_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('cricketers/', cricketers, name='cricketers'),
    path('cricketers/<role>/', cricketers, name='cricketers'),
    path('cricketer/<int:id>/', cricketer, name='cricketer'),
    path('teams/', teams, name='teams'),
    path('teams/<type>/', teams, name='teams'),
    path('team/<int:id>/', team, name='team'),
    path('matches/', matches, name='matches'),
    path('livematches/', liveMatches, name='livematches'),
]