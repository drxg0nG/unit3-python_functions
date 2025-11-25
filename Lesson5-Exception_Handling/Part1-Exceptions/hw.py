# 3 - Safe Contact Lookup
def get_phone_number(contacts, name):
    try:
        return contacts[name]
    except KeyError:
        return "Contact not found"

contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}
print(get_phone_number(contacts, "Mom")) # Output: "555-0123"

contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}
print(get_phone_number(contacts, "Boss")) # Output: "Contact not found"

contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}
print(get_phone_number(contacts, "Best Friend")) # Output: "555-0125"


# 4 - Safe Playlist Access
def get_song(playlist, position):
    try:
        return playlist[position]
    except IndexError:
        return "Position out of range"
    except TypeError:
        return "Position must be an integer"

playlist =["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, 2)) # Output: "Song C"

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, 20)) # Output: "Position out of range"

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, "first")) # Output: "Position must be an integer"


# 5 - Test Average Score Calculator
def calculate_test_average(scores):
    try:
        return f"{round(sum(scores) / len(scores), 2)}"
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "Invalid score data"

print(calculate_test_average([88, 92, 76, 95, 84])) # Output: 87.0

print(calculate_test_average([78.5, 92.0, 85.5])) # Output: 85.33

print(calculate_test_average([])) # Output: 0

