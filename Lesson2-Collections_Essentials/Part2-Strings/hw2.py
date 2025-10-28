# 1
print("Solution: john.split", "gmail.com")

# 2
print("Solution: tqbf")

# 3
def extract_domain(email):
    symbol = "@"
    domain = ""
    if email.count(symbol) == 1:
        domain = email.split("@")[-1]
        return domain.lower()
    else:
        return "Invalid Email"
print(extract_domain("john@gmail.com")) # gmail.com
print(extract_domain("JANE@YAHOO.COM")) # yahoo.com
print(extract_domain("missing.at.sign.com")) # Invalid Email
print(extract_domain("too@@many@signs.com")) # Invalid Email

# 4
print("Solution: 123456")

# 5
print("MY_NAME")

# 6
print("banana")

# 7
def filter_numbers(text):
    filtered_text = []
    for char in text:
        if not char.isdigit():
            filtered_text.append(char)
    return ''.join(filtered_text)
print(filter_numbers("Hello123World456")) # "HelloWorld"
print(filter_numbers("Test 1 2 3")) # "Test   "
print(filter_numbers("Price: $29.99")) # "Price: $"
print(filter_numbers("No numbers here!")) # "No numbers here!"

# 8
print("Solution: https://example.com/users/profile")

# 9
def count_character_types(text):
    letters = 0
    digits = 0
    spaces = 0
    for char in text:
        if 'a' <= char.lower() <= 'z':
            letters += 1
        elif '0' <= char <= '9':
            digits += 1
        elif char == ' ':
            spaces += 1
    return f"letters: {letters}, digits: {digits}, spaces: {spaces}"
print(count_character_types("Hello 123")) # {"letters": 5, "digits": 3, "spaces": 1}
print(count_character_types("Test2024!")) # {"letters": 4, "digits": 4, "spaces": 0}
