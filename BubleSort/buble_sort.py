# buble sort function
def buble_sort(array: list[int]) -> list[int]:
   
    """
    Sorts the given array using buble sort algorithm

    Parameters
    ----------
    array : list
        The list of elements to sort

    Returns
    -------
    The sorted array

    Time Complexity
    ----------------
        time complexity: Best Case: O(n) when array is already sorted
        Average/Worst Case: O(n²)

    Space Complexity
    ----------------
        space complexity: O(1)
    """
    
    n = len(array)

    for i in range(n):
        swapped = False  # Optimization flag
                                            
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # Swap elements
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                
        # If no swaps occurred, array is sorted
        if not swapped:
            break
            
    return array

# initializing array
array = [2,3,1,4,7,8,10,9,6,5]

# calling buble_sort function
print(*buble_sort(array))