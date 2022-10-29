# Binary search implementation in Python

"""
Searches for {item} in {list} using binary search

PARAM List: list – List to search. PRECONDITION {list} sorted in ascending order
PARAM Any: item – item to search for

RETURN Integer/None – Integer if {item} in {list}, None if not

"""
def binary_search(list, item):

    # Search space boundaries
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (int)((low + high) / 2) # make sure index is an integer
        guess = list[mid]

        # Found {item}!
        if guess == item:
            return mid

        # {item} LOWER, shift upper bound
        elif item < guess:
            high = mid - 1

        # {item} HIGHER, shift lower bound
        else:
            low = mid + 1
    
    return None
