# The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it
# down into smaller arrays, and then building the array back together the correct way so that it is sorted.
# Divide: The algorithm starts with breaking up the array into smaller and 
# smaller pieces until one such sub-array only consists of one element.
# Conquer: The algorithm merges the small pieces of the array back together 
# by putting the lowest values first, resulting in a sorted array.
# The breaking down and building up of the array to sort the array is done recursively.

# Time complexity: O(n * log n)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedRight = mergeSort(rightHalf)
    sortedLeft = mergeSort(leftHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)