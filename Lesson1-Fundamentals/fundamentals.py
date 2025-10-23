"""
Python Functions - Unit 3 Lesson 1 Starter Code
"""

def calculate_score(points, bonus):
    total = points + bonus
    print("Score Calculated!")
    return total

# =============================================================================
# CODE ALONG 1: SOCIAL MEDIA ENGAGEMENT
# =============================================================================

# TODO: Create calculate_engagement function
# Parameters: likes, shares, comments
# Return: total engagement (sum of all three)
def calculate_engagement(likes, shares, comments):
    total_engagement = likes + shares + comments
    return total_engagement

# Test it
print(calculate_engagement(500, 50, 200))  # Should print: 750


# =============================================================================
# PRACTICE 1: FORMAT HANDLE
# =============================================================================

# TODO: Create format_handle function
# Parameter: username (string)
# Return: username with @ prefix
# Example: format_handle("nasa") returns "@nasa"
def format_handle(username):
    return "@" + username

# Test it
print(format_handle("nasa"))    # Should print: @nasa
print(format_handle("tswift"))  # Should print: @tswift


# =============================================================================
# PRACTICE 2: IS TRENDING
# =============================================================================

# TODO: Create is_trending function
# Parameter: likes (number)
# Return: True if likes > 1000, else False
def is_trending(likes):
    return likes > 1000

# Test it
print(is_trending(500))   # Should print: False
print(is_trending(2500))  # Should print: True


# =============================================================================
# CODE ALONG 2: MUSIC TIER SYSTEM
# =============================================================================

# TODO: Create get_tier_perks function
# Parameter: subscription_type (string)
# Return: daily skips based on tier
#   - "premium" -> 999
#   - "student" -> 10
#   - "free" -> 3
#   - anything else -> 0
def get_tier_perks(subscription_type):
    if subscription_type == "premium":
        return 999
    elif subscription_type == "student":
        return 10
    elif subscription_type == "free":
        return 3
    else:
        return 0

# Test it
print(get_tier_perks("premium"))  # Should print: 999
print(get_tier_perks("student"))  # Should print: 10
print(get_tier_perks("free"))     # Should print: 3


# =============================================================================
# PRACTICE 3: VIDEO QUALITY
# =============================================================================

# TODO: Create get_video_quality function
# Parameter: bandwidth (number in Mbps)
# Return: video quality based on speed
#   - Over 5 Mbps -> "1080p"
#   - 2-5 Mbps -> "720p"
#   - Under 2 Mbps -> "480p"
def get_video_quality(bandwidth):
    if bandwidth > 5:
        return "1080p"
    elif 2 <= bandwidth <= 5:
        return "720p"
    else:
        return "480p"

# Test it
print(get_video_quality(1))   # Should print: 480p
print(get_video_quality(3))   # Should print: 720p
print(get_video_quality(10))  # Should print: 1080p


def calculate_discount(price, member_status):
    if member_status == "premium":
        discount = 0.30
    elif member_status == "standard":
        discount = 0.15
    elif member_status == "guest":
        discount = 0.0
    final_price = price * (1 - discount)
    return final_price

print(calculate_discount(100, "premium"))   # Should print: 70.0
print(calculate_discount(100, "standard"))  # Should print: 85.0
print(calculate_discount(100, "guest"))     # Should print: 100.0


def count_vowels(text):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o' , 'u']
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count

print(count_vowels("HEllo World"))
print(count_vowels("Python"))
print(count_vowels("AEIOU"))

def validate_password(password):
    if len(password) < 8:
        return False
    elif password.isdigit():
        return True
print(validate_password("1asdfhas7"))    # Should print: False