# binary search function
def binary_search(array: list[int] , target: int) -> int:

    """
    Searches for the target in the given array using binary search algorithm

    Parameters
    ----------
    array : list
        The list of elements to search in
    target : int
        The element to search for

    Returns
    -------
    The index of the target in the array if found, -1 otherwise
    """
    
    n = len(array)
    L , R = 0 , n - 1

    while L <= R:

        mid = (L + R) // 2

        # if target found
        if array[mid] == target:
            return mid
        
        # if target > mid we eliminate Left half
        elif array[mid] < target:
            L = mid + 1       # search in the right half

        # if target > mid we eliminate Right half
        else:
            R = mid - 1      # search in the left half 

    # if target not found
    return -1

# initializing array along with target
array = [1,2,3,4,5,6,7,8,9,10]

try:
    target = int(input("Enter the number to search: "))

except ValueError:
    print("Invalid input")
    exit()

# calling binary_search function
print('target found at index: ' + str(binary_search(array , target)) if binary_search(array , target) != -1 else 'target not found')