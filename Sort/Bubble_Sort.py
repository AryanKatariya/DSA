def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place
        for j in range(0,n-i-1):
            # traverse the array from 0 to n-i-1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)
