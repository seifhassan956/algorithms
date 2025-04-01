# fn for quick sort edit in place
def quick_sort(array: list[int] , start: int , end: int) -> None:
    """
    Sorts the given array in place using quick sort algorithm

    Parameters
    ----------
    array : list [int]
        The list of elements to sort

    start : int
        The starting index of the array

    end : int
        The ending index of the array

    Returns
    -------
        None the sorted array is modified in place

    Time Complexity
    ----------------
        time complexity: - best/average case: O(nlogn)
                         - if array is sorted: ** worst case O(n²) **

    Space Complexity
    ----------------
        space complexity: O(log n) ** recursion stack **
    """

    # base case if 0 elements or 1 element
    if start >= end:
        return
    
    # select pivot
    pivot = array[end]

    i = start - 1

    # swap (i+1) with j if element < pivot
    for j in range(start , end):
        if array[j] < pivot:
            i += 1
            array[i] , array[j] = array[j] , array[i]

    # specify new pivot = i + 1 and swap it with old pivot
    i += 1
    array[i] , array[end] = array[end] , array[i]

    pivot = i
    
    # divide and conquer the list by recursion
    quick_sort(array , start , pivot-1)
    quick_sort(array , pivot+1 , end)

# initialize an array
array = [2,3,1,4,7,8,10,9,6,5]
n = len(array)

# calling quick_sort function
quick_sort(array , 0 , n-1)

# printing the sorted array
print(*array)