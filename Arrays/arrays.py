# To find the least number in the array.
# Time complexity: O(1)

my_array = [7, 12, 9, 4, 11]

minVal = my_array[0]

for num in my_array:
    if num < minVal:
        minVal = num
    
print("Least number in the array : ", minVal)