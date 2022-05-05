# Tuples are immutable objects in Python, meaning that they cannot be changed, unlike lists. Because tuples are immutable, they cannot be copied. Some operators can work on lists, but not on tuples.
# Elements of a tuple can be of any data type. This makes a tuple versatile

# Qn 1: Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

# Qn 2: Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

# Qn 3: Create a tuple with a single item 50
tuple1 = ('50',)
print(tuple1[0])

# Qn 4: Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

# Qn 5: Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

# Qn 6: Copy specific elements from one tuple to a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)

# Qn 7: Modify the tuple
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

# Qn 8: Sort a tuple of tuples
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple1 = sorted(tuple1, key=lambda x: x[1])
print(tuple1)

# Qn 9: Count the number of occurrences of item 50 in the tuple
tuple1 = (50, 10, 60, 70, 50)
item_count = tuple1.count(50)
print(item_count)