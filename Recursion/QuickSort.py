# def partition(a,si,ei):
#     pivot = a[si]
#     # find number of element  smaller than pivot_index
#     c = 0
#     for i in range(si,ei+1):
#         if a[i] < pivot:
#             c = c+ 1
#     a[si+c],a[si] = a[si],a[si+c]
#     pivot_index = si+c
#
#     i = si
#     j = ei
#     while i<j:
#         if a[i] < pivot:
#             i = i+1
#         elif a[j] >= pivot:
#             j = j-1
#         else:
#             a[i],a[j] = a[j],a[i]
#             i = i+1
#             j = j-1
#         return pivot_index
#
# def quickSort(a,si,ei):
#     if len(a) == 1:
#         return a
#
#     if si < ei:
#         pivot_index = partition(a,si,ei)
#         quickSort(a,si,pivot_index-1)
#         quickSort(a,pivot_index+1,ei)
#
#
# a = [6,10,9,8,7,1,3,5,4,2]
# partition(a,0,(len(a)-1))
# print(a)


    def partition(arr, low, high):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):

            if arr[j] <= pivot:

                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)




def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr

	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr = [6,10,9,8,7,1,3,5,4,2]
partition(arr,0,len(arr)-1)
print("Array after partition function",arr)
quickSort(arr, 0, len(arr)-1)
print("Array after Quic Sort",arr)
