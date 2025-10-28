def create_username(first_name, last_name):
    username = f"{first_name}_{last_name}".lower()
    return username
print(create_username("John", "Smith"))  # "john_smith"

def check_email(email):
    return "@" in email and ".com" in email or ".COM" in email
print(check_email("test@gmail.com"))  # True
print(check_email("user@yahoo.COM"))  # False
print(check_email("invalid.com"))  # False
print(check_email("test@school.edu"))  # False

def create_slug(title):
    return title.strip().replace(" ", "-").lower()
print(create_slug("My First Blog Post"))
print(create_slug("  Python Tutorial  "))
