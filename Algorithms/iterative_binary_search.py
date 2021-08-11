# Function to determine if a target (target) exists in a SORTED list (list) using an iterative binary search algorithm
def iterative_binary_search(list, target):

    # Determines the search space
    first = 0
    last = len(list) - 1

    # Loops through the search space
    while first <= last:

        # Updates the midpoint in the search space
        midpoint = first + (last - first) // 2

        # Compares target to the midpoint and returns midpoint if true
        if target == list[midpoint]:
            return midpoint

        # Removes all elements in the right side of the search space if target is lower than the midpoint value
        elif target < list[midpoint]:
            last = midpoint - 1

        # Removes all elements in the left side of the search space if target is higher than the midpoint value
        else:
            first = midpoint + 1

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
result = iterative_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
verify(result)

# Example case for if target does not exist in the list
result = iterative_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13)
verify(result)
