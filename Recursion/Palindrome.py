def helper(a,s,e):
    if s == e:
        return True
    if (a[s] != a[e]):
        return False
    if s < e+1:
        return helper(a,s+1,e-1)


def Palindrome(a):
    # l = len(a)
    # if l == 0:
    #     return True

    return helper(a,0,len(a)-1)

a = "arya"
print(Palindrome(a))
