import sqlite3
db = sqlite3.connect("app.db")
cursor = db.cursor()


row = cursor.execute("SELECT * FROM app_data")



class Team:

    def __init__(self, name):
        self.score = 1000
        self.team_name = name
        self.members = []

    def add_member(self, player):
        self.members.append(player)
        self.score -= player_value[player]
        if self.score != 0:
            self.score += player_value[player]
            print("Can't add player")


    def delete_member(self, player):
        self.current_team.remove(player)

def new_team ():
    name = ""
    new_team = Team(name)

def calculate_points(row):
    points = 0.0
    score = row[1]
    try: strike_rate = float(row[1])/float(row[2])
    except : strike_rate = 0
    fours, sixes = float(row[3]), float(row[4])
    twos = int((score - 4*fours - 6*sixes)/2)
    wickets = 10*float(row[8])
    try:
        economy = float(row[7])/(float(row[5])/6)
    except:
        economy = 0
    Fielding = float(row[9]) + float(row[10]) + float(row[11])

    points += (fours + 2*sixes + 10*Fielding + twos + wickets)
    if score > 100: points += 10
    elif score >= 50: points += 5
    if strike_rate > 1: points += 4
    elif strike_rate >= 0.8 : points += 2
    if wickets >= 5 : points += 10
    elif wickets > 3: points += 5
    if economy >= 3.5 and economy <= 4.5 : points += 4
    elif economy >= 2 and economy < 3.5: points += 7
    elif economy < 2: points += 10

    return points


Available_players = []
Total_points = 1000
player_points = {}

Avail_batsman, Avail_bowler, Avail_Allrounder, Avail_WicketKeeper = [], [], [], []
player_value = {}
for row in cursor.execute("SELECT * FROM app_data"):
    Available_players.append(row[0])
    player_name,ctg = row[0],row[-1]
    if (ctg == "BAT") : Avail_batsman.append(player_name)
    elif (ctg == "BWL") : Avail_bowler.append(player_name)
    elif (ctg == "AR") : Avail_Allrounder.append(player_name)
    elif (ctg == "WK") : Avail_WicketKeeper.append(player_name)

    player_points[player_name] = calculate_points(row)
    player_value[player_name] = row[-2]
print(player_value)




BAT, BWL, AR, WK = len(Avail_batsman), len(Avail_bowler), len(Avail_Allrounder), len(Avail_WicketKeeper)


''' RULES :
player scored faced fours sixes bowled maiden given wkts catches stumping ro  value ctg
0       1       2    3      4       5   6       7    8      9       10     11  12   13

Batting: 1 point for 2 runs scored
         Additional 5 points for half century
         Additional 10 points for century
         2 points for strike rate (runs/balls faced) of 80-100
         Additional 4 points for strike rate>100
         1 point for hitting a boundary (four) and 2 points for over boundary(six)

Bowling: 10 points for each wicket
         Additional 5 points for three wickets per innings
         Additional 10 points for 5 wickets or more in innings
         4 points for economy rate (runs given per over) between 3.5 and 4.5
         7 points for economy rate between 2 and 3.5
         10 points for economy rate less than 2

Fielding:
        10 points each for catch/stumping/run out '''
