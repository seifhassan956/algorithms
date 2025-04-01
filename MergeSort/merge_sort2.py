# fn for merge sort
def merge_sort(array: list[int]) -> None:
    """
    Sorts the given array in place using the merge sort algorithm.

    Parameters
    ----------
    array : list[int]
        The list of integers to be sorted. May contain duplicate values.

    Returns
    -------
    list[int]
        A new list containing all elements from the input array in sorted order.

    Time Complexity
    ---------------
    - Best case: O(n log n)
    - Average case: O(n log n)
    - Worst case: O(n log n)
    - Note: ** Merge sort maintains consistent performance regardless of input order. **

    Space Complexity
    ---------------
    - O(n)
    - Requires additional space proportional to the input size for merging.
    """

    if len(array) > 1:

        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, array)

# Merge two sorted lists (left, right):
def merge(left: list[int] , right: list[int] , array: list[int]) -> None:  
    """
    Merges two sorted lists into one sorted list.

    Parameters
    ----------
    left : list[int]
        First sorted list to merge

    right : list[int]
        Second sorted list to merge

    array : list[int]
        The original array

    Returns
    -------
    nothing the array is modified in place
    """
    
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

# initializing array
array = [2,3,1,4,7,8,10,9,6,5]

# calling merge_sort function
merge_sort(array)

# printing the new sorted array
print(array)