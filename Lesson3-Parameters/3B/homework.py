# 1
def combine_values(*args):
    result = 1
    for value in args:
        result *= value
    return result

print(combine_values(2, 3, 4)) # 24
print(combine_values(5)) # 5
print(combine_values()) # 1


# 2
def merge_details(label,**info):
    result = {"label": label}
    result.update(info)
    return result

merge_details("ItemA", size="Large", cost=12.50) # {"label": "ItemA", "size": "Large", "cost": 12.50}
merge_details("UserX") # {"label": "UserX"}

# 3
print("8, 10, 0")

# 4
print('"Alpha", x=1, y=2, "count: 2')
print('"Beta", "count: 0')
