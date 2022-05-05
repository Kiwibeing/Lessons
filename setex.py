# Qn 1: Add a list of elements to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)

# Qn 2: Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

# Qn 3: Get only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))

# Qn 4: Update the first set with items that don't exist in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))

# Qn 5: Remove items from the set at once
set1 = {10, 20, 30, 40, 50}
remove_set = {10, 20, 30}
print(set1.difference(remove_set))

# Qn 6: Return a new set of elements in set 1 and 2, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))

# Qn 7: Check if two sets have any common elements. If yes, display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
    print('The two sets have no common element.')
else:
    print("Two sets have items in common.")
    print(set1.intersection(set2))

# Qn 8: Update set 1 by adding elements from set 2, except common elements
# symmetric_difference: all elements that are in exactly one of the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))

# Qn 9: Remove items that are not common in set 1 and 2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)