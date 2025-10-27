# Starting with messy user input:
announcement = "  BERGEN TECH robotics meeting TODAY!  "


def format_course_code(code):
    return code.strip().upper()
print(format_course_code("  webdev101  "))  # Output: "WEBDEV101"
print(format_course_code("  Python202  "))  # Output: "PYTHON202"

def count_hashtags(post):
    return post.count('#')
print(count_hashtags("Great game today! #BergenTech #GoGamrz #Pride"))
print(count_hashtags("Meeting tomroow in room 205"))


