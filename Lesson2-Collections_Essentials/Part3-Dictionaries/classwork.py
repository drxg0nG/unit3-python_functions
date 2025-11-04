# 1
print('"key_a": "value1", "key_b": 150, "key_c": False, "key_d": 50')
print('False')

# 2
print("120")
print("60")

# 3
def get_user_bio(user):
    bio = user.get("bio")
    if bio:
        return user["bio"]
    else:
        return "No bio avaliable"
print(get_user_bio({"username": "coder", "bio": "Python enthusiast"})) # "Python enthusiast"
print(get_user_bio({"username": "newbie"})) # "No bio available"

# 4
print("60")
print("160")

# 5
print("1")

# 6
def get_total_engagement(post):
    if post.get("likes"):
        likes = post["likes"]
    else:
        likes = 0
    if post.get("comments"):
        comments = post["comments"]        
    else:
        comments = 0
    if post.get("shares"):
        shares = post["shares"]
    else:
        shares = 0
    return likes + comments + shares
print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10})) # 130
print(get_total_engagement({"likes": 50, "comments": 5})) # 55
print(get_total_engagement({"views": 1000})) # 0

# 7
print("3")
print("3")

# 8
{'key1': 'value1', 'key2': 200, 'key3': 50}
{'key1': 'value1', 'key2': 100, 'key4': True}

# 9
def find_more_followers(users):
    most_followers = 0
    top_user = ""
    for user in users:
        if user["followers"] > most_followers:
            most_followers = user["followers"]
            top_user = user["username"]
    return top_user

users = [
    {"username": "alex", "followers": 1000},
    {"username": "sam", "followers": 5000},
    {"username": "jordan", "followers": 3000},
]

print(find_more_followers(users))  # "sam"
