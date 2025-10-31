# MY way
def santize_filename(filename):
    filename = filename.strip().lower().replace(' ', '_')
    if len(filename) <= 50:
        result = ""
        for char in filename:
            if char.isalnum() or char in ".-_":
                result += char
        filename = result
        if filename.endswith(".txt"):
            return filename
        else:
            if filename[:-4] == ".":
                new_filename = filename[:-4] + ".txt"
                filename = new_filename
            else:
                filename += ".txt"
    else:
        return "Invalid"
    return filename
print(santize_filename("Ancient Scroll.txt"))
print(santize_filename("Quest 2042! (Epic)"))
print(santize_filename("notes"))
print(santize_filename("X"*60))
