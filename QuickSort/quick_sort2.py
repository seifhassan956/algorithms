# fn for quick sort edit in new array
def quick_sort(arr):
    """
    Sorts the given array using quick sort algorithm

    Parameters
    ----------
    arr : list
        The list of elements to sort

    Returns
    -------
    The new sorted array
    
    Time Complexity
    ----------------
        time complexity: - best/average case: O(nlogn)
                         - if array is sorted/nearly sorted: ** worst case O(n²) **

    Space Complexity
    ----------------
        space complexity: O(log n) ** recursion stack **
    """

    if len(arr) <= 1:
        return arr  # Base case: already sorted
    
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot

    left = [x for x in arr if x < pivot]   # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements larger than pivot
    
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort

# initialize an array
array = [2,3,1,4,7,8,10,9,6,5]
n = len(array)

# printing the new sorted array
print(*quick_sort(array))