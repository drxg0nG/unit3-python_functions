def filter_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(filter_evens([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(filter_evens([10, 15, 20, 25])) # [10, 20]
print(filter_evens([1, 3, 5])) # []

def list_stats(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total / len(numbers)
    return {
        "max": maximum,
        "min": minimum,
        "average": average
    }

print(list_stats([10, 20, 30, 40, 50]))  # {'max': 50, 'min': 10, 'average': 30.0}
print(list_stats([5, 15, 25]))  # {'max': 25, 'min': 5, 'average': 15.0}
print(list_stats([]))  # None


