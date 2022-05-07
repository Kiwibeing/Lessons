sample_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# List construction using ranges
list = list(range(-1. 4))

# Print something a fixed number of times
def cheer():
  n = get_input("Number of cheers: ")
  # Simple convention to use is "_" when there isn't a point in specifying the element
  for _ in range(n):
    print("Go HC!)
