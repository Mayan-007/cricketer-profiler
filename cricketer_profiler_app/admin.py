from django.contrib import admin
from cricketer_profiler_app.models import *

# Register your models here.
class cricketerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('name', 'country')
    search_fields = ('name', 'country')

admin.site.register(Cricketer, cricketerAdmin)
    
admin.site.register(Coach)

class matchFormatAdmin(admin.ModelAdmin):
    list_display = ('match_format',)
    list_filter = ('match_format',)
    search_fields = ('match_format',)
    
admin.site.register(MatchFormat, matchFormatAdmin)

class battingCareerAdmin(admin.ModelAdmin):
    list_display = ('cricketer', 'match_format', 'matches', 'innings')
    list_filter = ('cricketer', 'match_format', 'matches', 'innings', 'not_outs', 'runs', 'highest_score', 'average', 'balls_faced', 'strike_rate', 'hundreds', 'fifties', 'fours', 'sixes')
    
admin.site.register(BattingCareer, battingCareerAdmin)

class bowlingCareerAdmin(admin.ModelAdmin):
    list_display = ('cricketer', 'match_format', 'matches', 'innings')
    list_filter = ('cricketer', 'match_format', 'matches', 'innings', 'balls', 'runs', 'wickets', 'best_bowling_innings', 'best_bowling_match', 'average', 'economy', 'strike_rate', 'four_wickets', 'five_wickets')
    
admin.site.register(BowlingCareer, bowlingCareerAdmin)

class fieldingCareerAdmin(admin.ModelAdmin):
    list_display = ('cricketer', 'match_format')
    list_filter = ('cricketer', 'match_format', 'catches', 'stumpings')
    
admin.site.register(FieldingCareer, fieldingCareerAdmin)

class teamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'country')
    list_filter = ('team_name', 'country')
    search_fields = ('team_name', 'country')
    
admin.site.register(Team, teamAdmin)

class cricketerTeamAdmin(admin.ModelAdmin):
    list_display = ('cricketer', 'team')
    list_filter = ('cricketer', 'team')
    search_fields = ('cricketer', 'team')

admin.site.register(CricketerTeam, cricketerTeamAdmin)

class matchAdmin(admin.ModelAdmin):
    list_display = ('winner', 'match_format', 'team_1', 'team_2')
    list_filter = ('winner', 'match_format', 'team_1', 'team_2')
    search_fields = ('winner', 'match_format', 'team_1', 'team_2')

admin.site.register(Match, matchAdmin)
