# Qn 1: Reverse a list
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

# Qn 2: Concatenate 2 lists index wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
new_list = list(i + j for i, j in zip(list1, list2))
print(new_list)

# Qn 3: Turn every item in a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
square_numbers = [i * i for i in numbers]
print(square_numbers)

# Qn 4: Concatenate 2 lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [x + y for x in list1 for y in list2]
print(list3)

# Qn 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
number_set = set(zip(list1, list2[::-1]))
for group in number_set:
    x, y = group
    print(x, y)

# Qn 6: Remove empty string from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_list = [x for x in list1 if x != '']
print(new_list)

# Qn 7: Add new item to list after specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# Qn 8: Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

# Qn 9: Replace list's items with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
index_no = list1.index(20)
list1[index_no] = 200
print(list1)

# Qn 10: Remove all occurences of a specific item from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i == 20:
        list1.remove(i)
print(list1)
# or use list comprehension to create a function
list1 = [5, 20, 15, 20, 25, 50, 20]
def remove_value(list, number):
    return [i for i in list if i != number]
new_list = remove_value(list1, 20)
print(new_list)