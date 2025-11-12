# 1
print("23")

# 2
print("NEXUS")

# 3
players = {
    "phoenix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18}
}

def match_mvp(players):
    mvp = ""
    highest_kd = 0
    for player, stats in players.items():
        kd_ratio = stats["kills"] / stats["deaths"]
        if kd_ratio > highest_kd:
            highest_kd = kd_ratio
            mvp = player
    return mvp
print(match_mvp(players)) # "phoenix"
