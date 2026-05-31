# ---------------------------------------------------------
# MERGE SORT (DYNAMIC INPUT FROM USER)
# ---------------------------------------------------------

def merge_sort(arr):
    # Base case: if the list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index
    mid = len(arr) // 2

    # Divide the array into left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge both halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    """

    merged = []
    i, j = 0, 0

    # Compare elements and build sorted list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements (if any)
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# ------------------------------
# User provides input
# ------------------------------

# Ask user to enter numbers separated by space
user_input = input("Enter numbers separated by space: ")

# Convert input string into list of integers
arr = list(map(int, user_input.split()))

# Perform sorting
sorted_arr = merge_sort(arr)

# Display result
print("Sorted Array:", sorted_arr)