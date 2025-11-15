def calcualte_cart_total(*prices):
    """
    Calculate total for any number of items
    Parameters: vatiable number of price values
    Returns: total sum of all prices rounded to 2 decimals
    """

    # check if cart is empty
    if not prices:
        return "0.00"
    
    # sum of all prices
    total = sum(prices)
    return round(total, 2)

print(f"Empty Cart: {calcualte_cart_total()}")
print(f"1 Item: {calcualte_cart_total(19.99)}")
print(f"3 Item: {calcualte_cart_total(19.99, 12.34, 2.99)}")
print(f"4 Item: {calcualte_cart_total(19.99, 4.50, 7.99, 8.65)}")


def create_order(customer_name, **items):
    """Create an order with any menu items"""
    order = {
        "customer": customer_name,
        "items": items,
        "Quantity": len(items),
    }
    return order

# Different customers, different orders
order1 = create_order("Alex", pizza=2, soda=1, wings=12)
order2 = create_order("John", burger=1, soda=1, fries=2, nuggets=6)
order3 = create_order("Alice", salad=1)

print(f"Order 1: {order1}")
print(f"Order 2: {order2}")
print(f"Order 3: {order3}")


# Parameter order is strict
def function(required, *args, default=10, **kwargs):
    pass
