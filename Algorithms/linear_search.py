# Function to determine if a target (target) exists in a SORTED list (list) using a linear search algorithm
def linear_search(list, target):

    # Loops through the search space to find target, returns index of target if true
    for i in range(0, len(list) - 1):
        if target == list[i]:
            return i
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
result = linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
verify(result)

# Example case for if target does not exist in the list
result = linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13)
verify(result)
