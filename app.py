from cricket.player import Player
from cricket.team import Team
from cricket.field import Field
from cricket.match import Match
import random

# Creating fake data
# Adding the players
player1 = []
for i in range(10):
    player1.append(Player("Michael_"+str(i+1), round(random.random(), 1), round(random.random(), 1),
                          round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)))

player2 = []
for i in range(10):
    player2.append(Player("Edekin_"+str(i+1), round(random.random(), 1), round(random.random(), 1),
                          round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)))

# Adding players to teams
team1 = Team("Nigeria", player1)
team2 = Team("United Kingdom", player2)

# Showing the field
field = Field("Big", 0.9, 0.9, 0.9)

# Starting match simulation
total_overs = 2
match = Match(team1, team2, field, total_overs)
match.start_match()
