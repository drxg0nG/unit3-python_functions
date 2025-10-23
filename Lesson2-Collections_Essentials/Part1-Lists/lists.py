'''
FEATURE     JavaScript          PYTHON
create      [1, 2, 3]           [1, 2, 3]
add         .push(val)          .append(val)
remove      .pop()              .pop()
insert      .splice(i, 0, val)  .insert(i, val)
length      .length             len(list)
slice       .slice(i, j)        list[i:j]
index       [0]                 [0]
length()    .length             len(list)
maximum                         max(list)
minimum                         min(list)
total                           sum(list)
'''

# Creaing lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user123", True]
# Accessing elements
first_day = daily_likes[0]  # 500
last_day = daily_likes[-1]  # 400
third_day = daily_likes[2]  # 750
# Slicing (like JS slice())
first_three = daily_likes[0:3]  # [500, 600, 750]
last_two = daily_likes[-2:]  # [750, 400]

# Code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total_likes = sum(likes_list)
        max_likes = max(likes_list)
        min_likes = min(likes_list)
        average_likes = total_likes / len(likes_list)
        return {
            "total": total_likes,
            "max": max_likes,
            "min": min_likes,
            "average": average_likes
        }
    return "The list is empty."

# Format usernames - My way
def format_usernames(list):
    for name in range(len(list)):
        list[name] = "@" + list[name]
    return list
print(format_usernames(["nasa", "tswift", "netflix"]))  # ['@nasa', '@tswift', '@netflix']

# Format usernames - Teacher way
def format_usernames_teacher(handles):
    formatted = []
    for handle in handles:
        formatted.append("@" + handle)
    return formatted
print(format_usernames_teacher(["nasa", "tswift", "netflix"]))

# Filter trending posts
def filter_trending_posts(list):
    trending = []
    for likes in list:
        if likes > 1000:
            trending.append(likes)
    return trending
print(filter_trending_posts([500, 1200, 800, 1500, 600]))  # [1200, 1500]