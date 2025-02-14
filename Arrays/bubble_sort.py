# Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

# Flow:
# 1. Go through the array, one value at a time.
# 2. For each value, compare the value with the next value.
# 3. If the value is higher than the next one, swap the values so that the highest value comes last.
# 4. Go through the array as many times as there are values in the array.

# Time complexity: O(n * 2)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] =  my_array[j + 1], my_array[j]
            swapped = True
    if not swapped:
        break
print("Sorted array : ", my_array)

