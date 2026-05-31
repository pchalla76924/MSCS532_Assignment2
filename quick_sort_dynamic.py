# ---------------------------------------------------------
# QUICK SORT (DYNAMIC INPUT FROM USER)
# ---------------------------------------------------------

def partition(arr, low, high):
    """
    Partitions the array using the last element as pivot.

    Steps:
    1. Choose the last element as pivot.
    2. Move all elements smaller than pivot to the left.
    3. Place pivot in its correct position.
    """

    pivot = arr[high]   # Pivot element (last element)
    i = low - 1         # Index for smaller elements

    # Traverse array and rearrange elements
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    """
    Sorts the array using Quick Sort algorithm.

    Steps:
    1. Partition the array around pivot.
    2. Recursively sort left part.
    3. Recursively sort right part.
    """

    if low < high:

        # Get pivot index after partition
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before pivot
        quick_sort(arr, low, pivot_index - 1)

        # Recursively sort elements after pivot
        quick_sort(arr, pivot_index + 1, high)


# ------------------------------
# Taking input from user
# ------------------------------

# Input from user
user_input = input("Enter numbers separated by space: ")

# Convert string input to list of integers
arr = list(map(int, user_input.split()))

# Call Quick Sort
quick_sort(arr, 0, len(arr) - 1)

# Print result
print("Sorted Array:", arr)
