def firstindex(a,x):
    l = len(a)
    if l == 0:
        return -1

    if a[0] == x:
        return 0

    smallerList = a[1:]
    smallerListOutput = firstindex(smallerList,x)

    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput + 1

def firstindexBetter(a,x,si):
    l = len(a)
    if si == l:
        return -1

    if a[si] == x:
        return si

    smallerListOutput = firstindexBetter(a,x,si+1)
    return smallerListOutput


a = [1,2,4,5,6,7,8,9,7]
print(firstindexBetter(a,7,0))
