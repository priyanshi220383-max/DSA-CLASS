def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]   # current element
        j = i - 1

        # shift elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # place key at correct position
        arr[j + 1] = key

    return arr


# Example
arr = [8, 7, 1, 5, 3, 2, 9]
print(insertion_sort(arr))