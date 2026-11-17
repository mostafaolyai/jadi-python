teams = {
    "Iran": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
    "Spain": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
    "Portugal": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
    "Morocco": {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0},
}

# Each score is for the first team listed in the problem, followed by the second.
matches = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco"),
]

for first_team, second_team in matches:
    score = input().strip()
    first_goals, second_goals = map(int, score.split("-"))

    teams[first_team]["goal difference"] += first_goals - second_goals
    teams[second_team]["goal difference"] += second_goals - first_goals

    if first_goals > second_goals:
        teams[first_team]["wins"] += 1
        teams[first_team]["points"] += 3
        teams[second_team]["loses"] += 1
    elif first_goals < second_goals:
        teams[second_team]["wins"] += 1
        teams[second_team]["points"] += 3
        teams[first_team]["loses"] += 1
    else:
        teams[first_team]["draws"] += 1
        teams[second_team]["draws"] += 1
        teams[first_team]["points"] += 1
        teams[second_team]["points"] += 1

for team, stats in sorted(
    teams.items(), key=lambda item: (-item[1]["points"], -item[1]["wins"], item[0])
):
    print(
        f"{team}  wins:{stats['wins']} , loses:{stats['loses']} , "
        f"draws:{stats['draws']} , goal difference:{stats['goal difference']} , "
        f"points:{stats['points']}"
    )



