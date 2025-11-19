def search_query(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)

# 1 Return Type - None -> "No Value"
# Meaning: Abscence of a value, not set, not found
# Use: Missing data, search failures, optional parameters
result = None
print(result is None)  # True - identity check
print(result == None)  # True - equality check
print(not result)      # True - falsy check

# 2 Return Type - False = Boolean False
# Meaning: Explicit false condition, validation failure, neative result
# Use: Validation result, boolean operation, success/failure status
result = False
print(result is False) # True - identity check
print(not result)      # True - boolean check
print(result == 0)     # True - falsy check

# 3 Return Type - 0 = A Valid Number
# Meaning: 0 is VALID numberic value, not absence of value!
result = 0
print(result == 0)     # True - numeric check
print(not result)      # True - falsy check
print(result is None)  # False - different obj
print(result is False) # False - different obj


# Multiple Returns - python packs multiple returns into a tuple
def calculate(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

result = calculate(10, 5)
print(result)
print(type(result))

print(type(42))
print(type(42,))
no_parentheses = 1, 2, 3
print(type(no_parentheses))

area_result, perimeter_reesult = calculate(20, 6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_reesult}")



def analyze_grades(grades):
    if not grades:
        return (0, 0, 0, False)
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = average >= 60

    return f"{average}, {highest}, {lowest}, {passed}" 

# Test case 1: Normal grades
print(analyze_grades([85, 92, 78, 90]))
# Should return: (86.25, 92, 78, True)
 
# # Test case 2: Empty list
print(analyze_grades([]))
# Should return: (0, 0, 0, False)

# Test case 3: All same
print(analyze_grades([80, 80, 80]))
# Should return: (80.0, 80, 80, True)
