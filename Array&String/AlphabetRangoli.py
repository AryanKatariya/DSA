def print_rangoli(n):

    li =list(map(chr,range(97,123)))# NOTE: To generate list of [a-z]
    x = li[n-1::-1]+li[1:n]
    m = len("-".join(x))
    for i in range(1,n):
        print("-".join(li[n-1:n-i:-1]+li[n-i:n]).center(m,"-"))
    for i in range(n,0,-1):
        print("-".join(li[n-1:n-i:-1]+li[n-i:n]).center(m,"-"))

print_rangoli(5)
