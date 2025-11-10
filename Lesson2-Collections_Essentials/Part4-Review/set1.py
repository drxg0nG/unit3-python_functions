# 1
print("2300")

# 2
print("WOW WOW LFG")

# 3
def find_top_donors(donations):
    top_donations = ''
    top_amount = 0
    for name, amount in donations.items():
        if amount > top_amount:
            top_amount = amount
            top_donations = name
    return top_donations

donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

print(find_top_donors(donations))  # "lunar"
