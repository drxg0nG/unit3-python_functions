# Question 1: User Search with Tricky Trio
def search_user_database(data, success=False):
    result = ""
    message = ""
    if not data:
        result = None
        message = "No search query"
    elif data.strip() == result:
        result = None
        message = "No search query"
    else:
        for char in data:
            if not char.isalpha():
                result = False
                message = "Invalid characters"
                success = False
                break
            else:
                success = True
                if data == 'john':
                    result = 3
                    message = "Found 3 users"
                else:
                    result = 0
                    message = "No users found"
    return result, message, success


# TEST 1: Empty string → None (no value provided)
result, message, success = search_user_database("")
print(1)
print(result) # None
print(message) # "No search query"
print(success) # False

# TEST 2: Whitespace only → None (no value provided)
result, message, success = search_user_database(" ")
print(2)
print(result) # None
print(message) # "No search query"
print(success) # False

# TEST 3: Has numbers → False (operation failed)
result, message, success = search_user_database("user123")
print(3)
print(result) # False
print(message) # "Invalid characters"
print(success) # False

# TEST 4: Has special chars → False (operation failed)
result, message, success = search_user_database("user@email")
print(4)
print(result) # False
print(message) # "Invalid characters"
print(success) # False

# TEST 5: Valid but no results → 0 (valid count of zero)
result, message, success = search_user_database("admin")
print(5)
print(result) # 0
print(message) # "No users found"
print(success) # True ← Search worked! Just found nothing

# TEST 6: Valid with results → positive int
result, message, success = search_user_database("john")
print(6)
print(result) # 3 (or any positive number)
print(message) # "Found 3 users"
print(success) # True

print()

# Question 2: Book Collection Stats
def analyze_book_pages(books, has_long=False):
    count = len(books)
    if count == 0:
        return 0, 0, 0.0, False
    total = sum(books)
    avg = total / count
    for book in books:
        if book > 500:
            has_long = True
    return count, total, avg, has_long



# TEST 1: Mixed collection with one long book
count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print("Test 1")
print(count) # 4
print(total) # 1360
print(avg) # 340.0
print(has_long) # True (because 620 > 500)

# TEST 2: No long books
count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print("Test 2")
print(count) # 3
print(total) # 650
print(avg) # 216.67 (approximately)
print(has_long) # False (all books ≤ 500)

# TEST 3: Empty list - EDGE CASE!
count, total, avg, has_long = analyze_book_pages([])
print("Test 3")
print(count) # 0
print(total) # 0
print(avg) # 0.0
print(has_long) # False

# TEST 4: Exactly 500 pages - TRICKY!
count, total, avg, has_long = analyze_book_pages([500, 400, 300])
print("Test 4")
print(has_long) # False (500 is NOT > 500)

# TEST 5: Exactly 501 pages
count, total, avg, has_long = analyze_book_pages([501, 400, 300])
print("Test 5")
print(has_long) # True (501 IS > 500)
