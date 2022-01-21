def isSorted(lst):
    l = len(lst)
    if l == 0 or l == 1:
        return True

    if lst[0] > lst[1]:
        return  False

    smallerList = lst[1:]

    isSmallerListSorted = isSorted(smallerList)
    if isSmallerListSorted:
        return True
    else:
        return False

def isSortedBetter(a,si):
    l = len(a)
    if si == l or si == l-1:
        return True
    if a[si] > a[si+1]:
        return False
    isSmallerListSorted = isSortedBetter(a,si+1)
    return isSmallerListSorted


a =[2,1,4]
print(isSortedBetter(a,1))
