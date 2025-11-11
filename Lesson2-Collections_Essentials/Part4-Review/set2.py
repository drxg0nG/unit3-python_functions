# 1
print("4")
print("6700")

# 2
print("0x9F1aB3c...")

# 3
def portfolio_value(holdings, prices):
    total_value = 0
    for money, amount in holdings.items():
        if money in prices:
            total_value += amount * prices[money]
    return total_value

holdings = {"BTC": 0.5, "ETH": 8.2, "SOL": 50}
prices = {"BTC": 62400, "ETH": 2480, "SOL": 142}

print(portfolio_value(holdings, prices))