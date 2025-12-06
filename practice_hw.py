# 15
print("if not numbers: return 0")

# 16
print("C")

# 17
print(".strip(), .upper(), .split(), len")

# 18
def validate_password(password):
    if not password:
        return False, "Empty Password"
    if len(password) < 8:
        return False, "Too Short"
    else:
        return True, "Valid"
# Test
print(validate_password("")) # (False, "Empty password")
print(validate_password("abc")) # (False, "Too short")
print(validate_password("secure123")) # (True, "Valid")

# 19
def create_inventory(item_name, *quantities, location="Warehouse"):
    return {
        "item": item_name,
        "total": sum(quantities),
        "location": location,
    }

# Test
print(create_inventory("Widget", 10, 20, 15)) # {"item": "Widget", "total": 45, "location": "Warehouse"}
print(create_inventory("Gadget", 5, location="Store")) # {"item": "Gadget", "total": 5, "location": "Store"}

# 20
def safe_list_access(items, index):
    try:
        value = items[index]
        return value, True
    except IndexError:
        return None, False
    
# Test
print(safe_list_access([10, 20, 30], 1)) # (20, True)
print(safe_list_access([10, 20, 30], 10)) # (None, False)
print(safe_list_access([], 0)) # (None, False)


def grade_calculator(*scores, curve=0):
    try:
        average = sum(scores) / len(scores) + curve
    except ZeroDivisionError:
        return 0, "F"
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    return average, letter


print(grade_calculator(85, 90, 80)) # (85.0, "B")
print(grade_calculator(70, 75, curve=10)) # (82.5, "B")
print(grade_calculator()) # (0, "F")

