# bubble sort
def bubble_sort(lis:list):
    n = len(lis)
    for i in range (n):
        for j in range (n-1-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]= lis[j+1], lis[j]

# selection sort
def selection_sort(arr):
    n= len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]> arr[min_index]:
                min_index= j 
                arr [i],arr[min_index] = arr[min_index], arr[i]
            return arr

#--------------------insertion sort-----------------------------
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