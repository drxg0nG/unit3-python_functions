# 5
print("None")
print("15.0")

# 6
def make_notification(user, *messages, urgent=False):
    if urgent:
        return f"URGENT: {user} - {', '.join(messages)}"
    return f"{user} - {', '.join(messages)}"
    
print(make_notification("admin", "Server down!", urgent=True)) # URGENT: admin - Server down!
print(make_notification("user", "Welcome", "Check inbox"))

# 7
print("SELECT name, email FROM users LIMIT 10")
print("SELECT * FROM logs WHERE level='error' LIMIT 5")
    
# 8
def log_action(actor, *actions, timestamp=None, **context):
    actions_str = ', '.join(actions)
    context_str = ', '.join(f"{key}={value}" for key, value in context.items())
    if context_str:
        return f"{actor}: {actions_str} | {context_str}"
    return f"{actor}: {actions_str}"

print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4")) # bot: login, scan | source=API, ip=1.2.3.4
