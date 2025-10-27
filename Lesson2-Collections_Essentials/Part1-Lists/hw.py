# 1
def remove_duplicates(items):
    seen = []
    result = []
    for item in items:
        if item not in seen:
            seen.append(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4])) # [1, 2, 3, 4]
print(remove_duplicates(["a", "b", "a", "c"])) # ['a', 'b', 'c']
print(remove_duplicates([5, 5, 5])) # [5]
print(remove_duplicates([])) # []


# 2
def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

print(find_common([1, 2, 3], [2, 3, 4])) # [2, 3]
print(find_common(["a", "b"], ["c", "d"])) # []
print(find_common([1, 1, 2], [2, 2, 3])) # [2]
print(find_common([], [1, 2])) # []


# 3
def reverse_sublists(data, size):
    result = []
    for i in range(0, len(data), size):
        sublist = data[i:i+size]
        reversed_list = []
        for item in sublist:
            reversed_list.insert(0, item)
        result.extend(reversed_list)
    return result

print(reverse_sublists([1, 2, 3, 4, 5, 6], 2)) # [2, 1, 4, 3, 6, 5]
print(reverse_sublists([1, 2, 3, 4, 5], 3)) # [3, 2, 1, 5, 4]
print(reverse_sublists([1, 2, 3, 4], 1)) # [1, 2, 3, 4]
print(reverse_sublists([1, 2, 3], 5)) # [3, 2, 1]


# 4
def rotate_list(items, positions):
    n = len(items)
    positions = positions % n
    rotated = []
    for i in range(n):
        new_index = (i - positions) % n
        rotated.append(items[new_index])
    return rotated

print(rotate_list([1, 2, 3, 4, 5], 2)) # [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3, 4, 5], -2)) # [3, 4, 5, 1, 2]
print(rotate_list([1, 2, 3], 0)) # [1, 2, 3]
print(rotate_list([1, 2, 3], 5)) # [2, 3, 1]
