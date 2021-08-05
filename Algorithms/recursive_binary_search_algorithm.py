# Function to determine if a target (target) exists in a SORTED list (list) using a recursive binary search algorithm
def recursive_binary_search(list, target, first, last):

    # Base condition
    if first > last:
        return None

    # Updates the midpoint in the search space
    midpoint = first + (last - first) // 2

    # Compares target to midpoint and returns midpoint if true
    if target == list[midpoint]:
        return midpoint

    # Removes all elements in the right side of the search space if target is lower than midpoint
    elif target < list[midpoint]:
        return recursive_binary_search(list, target, first, midpoint - 1)

    # Removes all elements in the left side of the search space if target is higher than midpoint
    else:
        return recursive_binary_search(list, target, midpoint + 1, last)


# Function to display the results of the implemented algorithm
def verify(index):

    # Notifies the user of where the target exists in the list if found
    if index is not None:
        print("The target was found at index", index, "in the list.")

    # Notifies the user that the target does not exist in the list
    else:
        print("The target was not found in the list.")


# Example case for if target exists in the list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(nums, 9, 0, len(nums) - 1)
verify(result)

# Example case for if target does not exist in the list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(nums, 13, 0, len(nums) - 1)
verify(result)
