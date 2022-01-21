def binarySearch(a,x,si,ei):
    if si > ei:
        return -1

    mid = (si+ei)//2

    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binarySearch(a,x,si,mid)
    else:
        return binarySearch(a,x,mid+1,ei)

a = [1,4,6,9,10,16,19,20,25,56]
print(binarySearch(a,10,0,len(a)))
