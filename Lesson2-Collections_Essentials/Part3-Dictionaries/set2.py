def calculate_engagement_rate(post):
    views = post.get("views", 0)
    if views:
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
    else:
        return "0.00"
    engagement = likes + comments + shares
    rate = (engagement / views) * 100.00
    return f"{rate:.2f}"

post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}
post2 = {"views": 0, "likes": 50, "comments": 10, "shares": 5}
post3 = {"likes": 50, "comments": 10, "shares": 5}
print(calculate_engagement_rate(post))  # "6.50"
print(calculate_engagement_rate(post2))  # "0.00"
print(calculate_engagement_rate(post3))  # "0.00"



