try:
    score = int(input("Enter Score: "))
except ValueError:
    print("Invalid Score!")
else:
    print(f"Valid Score Entered! {score}")


def parse_command(message):
    """Parse a Discord command like: !ban PlayerName 7days"""
    try:
        parts = message.split(' ')
        command = parts[0]
        target = parts[1]
        duration = parts[2]
    except IndexError:
        print("Invalid Command Format - missing parts")
    else:
        print("Command parsed successfully")
        if command.startswith("!"):
            print(f"Executing: {command}")
        return command, target, duration
    finally: # Runs no matter what
        print("This block runs no matter what!")

print(parse_command("!ban PlayerName 7days"))



