from django.db import models

class Cricketer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/cricketer/")
    description = models.TextField()
    country = models.CharField(max_length=50)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=50)
    height = models.IntegerField()
    player_role = models.CharField(max_length=50)
    batting_style = models.CharField(max_length=50)
    bowling_style = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Coach(models.Model):
    cricketer = models.ForeignKey(Cricketer, on_delete=models.CASCADE)

    def __str__(self):
        return self.cricketer.name
    
class MatchFormat(models.Model):
    match_format = models.CharField(max_length=50)

    def __str__(self):
        return self.match_format
    
class BattingCareer(models.Model):
    cricketer = models.ForeignKey(Cricketer, on_delete=models.CASCADE)
    match_format = models.ForeignKey(MatchFormat, on_delete=models.CASCADE)
    matches = models.IntegerField()
    innings = models.IntegerField()
    not_outs = models.IntegerField()
    runs = models.IntegerField()
    highest_score = models.IntegerField()
    average = models.FloatField()
    balls_faced = models.IntegerField()
    strike_rate = models.FloatField()
    hundreds = models.IntegerField()
    fifties = models.IntegerField()
    fours = models.IntegerField()
    sixes = models.IntegerField()

    def __str__(self):
        return self.cricketer.name
    
class BowlingCareer(models.Model):
    cricketer = models.ForeignKey(Cricketer, on_delete=models.CASCADE)
    match_format = models.ForeignKey(MatchFormat, on_delete=models.CASCADE)
    matches = models.IntegerField()
    innings = models.IntegerField()
    balls = models.IntegerField()
    runs = models.IntegerField()
    wickets = models.IntegerField()
    best_bowling_innings = models.CharField(max_length=50)
    best_bowling_match = models.CharField(max_length=50)
    economy = models.FloatField()
    average = models.FloatField()
    strike_rate = models.FloatField()
    four_wickets = models.IntegerField()
    five_wickets = models.IntegerField()

    def __str__(self):
        return self.cricketer.name
    
class FieldingCareer(models.Model):
    cricketer = models.ForeignKey(Cricketer, on_delete=models.CASCADE)
    match_format = models.ForeignKey(MatchFormat, on_delete=models.CASCADE)
    catches = models.IntegerField()
    run_outs = models.IntegerField()
    stumpings = models.IntegerField()

    def __str__(self):
        return self.cricketer.name
    
class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_logo = models.ImageField(upload_to="images/team/")
    team_format = models.ForeignKey(MatchFormat, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    captain = models.ForeignKey(Cricketer, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    home_ground = models.CharField(max_length=50)
    established = models.DateField()
    
    def __str__(self):
        return self.team_name

class CricketerTeam(models.Model):
    cricketer = models.ForeignKey(Cricketer, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cricketer.name

class Match(models.Model):
    match_date = models.DateField()
    match_format = models.ForeignKey(MatchFormat, on_delete=models.CASCADE)
    venue = models.CharField(max_length=50)
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_1")
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_2")
    result = models.CharField(max_length=20)
    toss_winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="toss_winner")
    match_winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="match_winner")
    player_of_the_match = models.ForeignKey(Cricketer, on_delete=models.CASCADE)
    team_1_batting_score = models.IntegerField()
    team_1_bowling_score = models.IntegerField()
    team_2_batting_score = models.IntegerField()
    team_2_bowling_score = models.IntegerField()
    
    def __str__(self):
        return self.team_1.team_name + " vs " + self.team_2.team_name
    