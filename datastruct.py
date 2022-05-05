# Qn 1: Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
new_l1 = [i for i in l1[1::2]]
new_l2 = [i for i in l2[0::2]]
l3 = new_l1 + new_l2
print(l3)

# Qn 2: Remove and add items in a list
list1 = [54, 44, 27, 79, 91, 41]
removed = list1.pop(4)
list1.insert(2, removed)
list1.append(removed)
print(list1)

# Qn 3: Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length = len(sample_list)
groups = int(length / 3)
start, end = 0, groups
for chunks in range(3):
    indexes = slice(start, end)
    chunk = sample_list[indexes]
    print("Chunk", chunks,  chunk)
    print("After reversing it: ", list(reversed(chunk)))
    start = end
    end += groups

# Qn 4: Count the occurences of each element from the list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_dict = {}
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)

# Qn 5: Create a Python set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

