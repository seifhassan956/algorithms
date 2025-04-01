# fn for merge sort
def merge_sort(array: list[int]) -> list[int]:
    """
    Sorts the given array using the merge sort algorithm.

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

    n = len(array)

    if n <= 1:
        return array
    
    # Divide
    mid = len(array) // 2
    
    left = merge_sort(array[:mid])  # Recursively sort left half
    right = merge_sort(array[mid:])  # Recursively sort right half

    # Merge
    return merge(left, right)

# Merge two sorted lists (left, right):
def merge(left: list[int] , right: list[int]) -> list[int]:  
    """
    Merges two sorted lists into one sorted list.

    Parameters
    ----------
    left : list[int]
        First sorted list to merge
        
    right : list[int]
        Second sorted list to merge

    Returns
    -------
    list[int]
        Combined new sorted list containing all elements from both inputs
    """
        
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# initializing array
array = [2,3,1,4,7,8,10,9,6,5]

# printing the new sorted array
print(*merge_sort(array))