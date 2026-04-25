def merge_sort(arr):
    # Base case: if list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Step 2: Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Step 3: Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
# ---------------------------------------------------------------------------
def quick_sort(arr, low, high):
    # This function sorts the array in-place using Quick Sort

    if low < high:
        # WHY: We only sort if there are at least 2 elements
        # If low >= high → 0 or 1 element → already sorted

        pi = partition(arr, low, high)
        # WHY: Partition function places pivot at correct position
        # and returns its index (pi = pivot index)

        quick_sort(arr, low, pi - 1)
        # WHY: Recursively sort left part (elements smaller than pivot)

        quick_sort(arr, pi + 1, high)
        # WHY: Recursively sort right part (elements greater than pivot)


def partition(arr, low, high):
    pivot = arr[high]
    # WHY: Choosing last element as pivot (simple and common method)

    i = low - 1
    # WHY: i keeps track of "smaller elements region"
    # Initially no elements are smaller → so i = low - 1

    for j in range(low, high):
        # WHY: j scans the array from low to high-1
        # We compare each element with pivot

        if arr[j] < pivot:
            # WHY: If current element is smaller than pivot,
            # it belongs to left side

            i += 1
            # WHY: Expand the "smaller elements" region

            arr[i], arr[j] = arr[j], arr[i]
            # WHY: Swap element to correct position in smaller region

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # WHY: Place pivot after last smaller element
    # Now pivot is at correct sorted position

    return i + 1
    # WHY: Return pivot index so recursion can divide array


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]

quick_sort(arr, 0, len(arr) - 1)
# WHY: Initial call → full array from index 0 to last

print(arr)
# Output: Sorted array