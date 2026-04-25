def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]   # choosing first element as pivot
    i = low + 1
    j = high

    while True:
        # Move i right until element > pivot
        while i <= j and arr[i] <= pivot:
            i += 1

        # Move j left until element <= pivot
        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  # swap
        else:
            break

    # Place pivot at correct position
    arr[low], arr[j] = arr[j], arr[low]

    return j


# Example
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)