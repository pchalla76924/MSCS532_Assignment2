# ---------------------------------------------------------
# QUICK SORT (STATIC INPUT INSIDE CODE)
# ---------------------------------------------------------

def partition(arr, low, high):

    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1        # Index of smaller element

    # Loop through the array
    for j in range(low, high):

        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:

            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    """
    Quick Sort main function.

    Recursively sorts the array by partitioning.
    """

    if low < high:

        # Partition the list and get pivot index
        pivot_index = partition(arr, low, high)

        # Sort elements before pivot
        quick_sort(arr, low, pivot_index - 1)

        # Sort elements after pivot
        quick_sort(arr, pivot_index + 1, high)


# ------------------------------
# Static input defined in code
# ------------------------------

arr = [38, 27, 43, 3, 9, 82, 10]

print("Original Array:", arr)

# Apply Quick Sort
quick_sort(arr, 0, len(arr) - 1)

# Display result
print("Sorted Array:", arr)