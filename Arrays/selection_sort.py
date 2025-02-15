# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

# Flow:
# 1. Go through the array to find the lowest value.
# 2. Move the lowest value to the front of the unsorted part of the array.
# 3. Go through the array again as many times as there are values in the array.

# Time complexity: O(n * 2)

my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i] 

print("Sorted array : ", my_array)