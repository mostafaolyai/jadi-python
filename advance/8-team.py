class Human:
    def __init__(self, name):
        self.name = name

class FootballPlayer(Human):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team


import random

teams = ["A", "B"]
players =  ["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد", "مصطفی", "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل", "بهروز", "شهروز", "سامان", "محسن"]

team_players = []
for name in players:
    team_players.append(FootballPlayer(name, random.choice(teams)))

for team in team_players:
    print(f"نام بازیکن : {team.name}: تیم: {team.team}")
