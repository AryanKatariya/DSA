def gSum(k):
    if k == 0:
        return 1

    a = gSum(k-1)
    return a + 1/2**k

print(gSum(4))
