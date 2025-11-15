def create_gamer(username, level, xp, rank, online):
    """Create a gamer profile."""
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online,
    }

player1 = create_gamer(username="BTStudent",
                       level=25,
                       rank="Gold",
                       xp=10000,
                       online=True,)
print(player1)


def send_message(sender, recipient, message, urgent):
    return f"{sender} -> {recipient}: {message} (Urgent: {urgent})"

msg = send_message(
    sender="Alex",
    recipient="Jordan",
    message="Check Discord",
    urgent=True,
)
print(msg)

def post_content(username, text, likes=0, retweets=0):
    return f"@{username}: {text} | ❤️: {likes} 🔄️: {retweets}"

print(post_content("techguru", "Python is amazing!"))


# *args - Accept any # of values
def sun_scores(*scores):
    """Sum ANY # of scores."""
    total = sum(scores)
    return total
print(sun_scores(10, 20, 30, 40))  # 100
