def safe_divide(a, b):
    try:
        result = a / b
        return result
    # except:
    #     print("Cannot divide by zero!")
    #     return None
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("That's not a valid number")
        return None
    except:
        print("An error occured...")

print(safe_divide(10, 2)) # 5.0
print(safe_divide(10, 0)) # Cannot divide by zero!


def safe_operations(a, b, lst, key, d):
    try:
        print(f"Divisionn Result: {a / b}") # ZeroDivisionError, TypeError
        print("Access list element:", lst[2]) # IndexError
        print("Access dictionary key:", d[key]) # KeyError
        print("Add numbers: {a + b}") # 
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except IndexError:
        print("Lisy index out of range")
    except KeyError:
        print(f"Key {key} not found in dictionary")
    except TypeError:
        print("Invalid types for operation")
    except Exception as e:
        print("Some other error occured", e)

print(10, 2, [1, 2], "Tom", {"John":15})


def calculate_price_per_item(cost, quantity):
    try:
        unit_price = cost / quantity
        return unit_price
    except ZeroDivisionError:
        return "No items to calculate"
print(calculate_price_per_item(100, 4))
print(calculate_price_per_item(50, 0))
print(calculate_price_per_item(25.50, 3))


def parse_age(age):
    try:
        num_age = int(age)
        return num_age
    except ValueError:
        return None

print(parse_age("25"))
print(parse_age("tweety-five"))



