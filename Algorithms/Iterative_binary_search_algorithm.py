# Function to determine if target integer(target) exists in a SORTED list(nums) using binary search algorithm
def binarySearch(nums, target):
    # Determines the search space
    first = 0
    last = len(nums) - 1

    # Loops through the search space
    while first <= last:
        # Updates the midpoint in the search space
        # first + (last - first) // 2, is used rather than, (last + first) // 2, in case of integer overflow
        mid = first + (last - first) // 2
        # Returns index of target if found
        if target == nums[mid]:
            return mid
        # Removes all elements in the right side of the search space if target is lower than the midpoint value
        elif target < nums[mid]:
            last = mid - 1
        # Removes all elements in the left side of the search space if target is higher than the midpoint value
        else:
            first = mid + 1
    # Returns None if target does not exist in the list
    return None


# Function to display the results of the implemented algorithm
def verify(index):
    # Notifies the user of where the target exists in the list if found
    if index is not None:
        print("The target was found at index", index, "in the list.")
    # Notifies the user that the target does not exist in the list
    else:
        print("The target was not found in the list.")


# Example case for if target exists in the list
result = binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
verify(result)

# Example case for if target does not exist in the list
result = binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13)
verify(result)
