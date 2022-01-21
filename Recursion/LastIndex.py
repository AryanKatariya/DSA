def LastIndex(a,x):
    l = len(a)
    if l == 0:
        return -1

    smallerList = [:l-1]
    smallerListOutput = LastIndex(smallerList,x)

    if smallerListOutput !== -1:
        return smallerListOutput + 1
    else:
        if a[0] == x:
            return 0
        else:
            return -1

def LastIndexBetter(a,x,si):
    l = len(a)
    if si == 0:
        return -1

    smallerListOutput = LastIndex(a,x,si+1)

    if smallerListOutput !== -1:
        return smallerListOutput
    else:
        if a[si] == x:
            return 0
        else:
            return -1
