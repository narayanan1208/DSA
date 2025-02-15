# The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element,
# and moves the other values so that lower values are on the left of the pivot element,
# and higher values are on the right of it.

# 1. Choose a value in the array to be the pivot element.
# 2. Order the rest of the array so that lower values than the pivot element
# are on the left, and higher values are on the right.
# 3. Swap the pivot element with the first element of the higher values
# so that the pivot element lands in between the lower and higher values.
# 4. Do the same operations (recursively) for the sub-arrays on the left
# and right side of the pivot element.

def median_of_three(array, low, high):
    mid = (low + high) // 2
    a, b, c = array[low], array[mid], array[high]

    # Find the median of three
    if (a <= b <= c) or (c <= b <= a):
        median_index = mid
    elif (b <= a <= c) or (c <= a <= b):
        median_index = low
    else:
        median_index = high

    # Swap median element with high (to use it as pivot)
    array[median_index], array[high] = array[high], array[median_index]
    return array[high]

def partition(array, low, high):
    # pivot = array[high]
    pivot = median_of_three(array, low, high)  # Use median-of-three as pivot
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array=array, low=low, high=high)
        quicksort(array=array, low=low, high=pivot_index-1)
        quicksort(array=array, low=pivot_index+1, high=high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
