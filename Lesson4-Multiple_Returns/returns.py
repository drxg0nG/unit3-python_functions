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
