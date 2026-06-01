# ---------------------------------------------------------
# MERGE SORT (STATIC WITH INPUT INSIDE)
# ---------------------------------------------------------

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Recursively sort left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    """

    merged = []
    i, j = 0, 0

    # Compare and merge elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# ------------------------------
# Static input defined in code
# ------------------------------

arr = [38, 27, 43, 3, 9, 82, 10]

print("Original Array:", arr)

# Sort the array
sorted_arr = merge_sort(arr)

# Display result
print("Sorted Array:", sorted_arr)