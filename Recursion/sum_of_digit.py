def SOD(a):
    if a == 0:
        return 0
    return (a % 10 + SOD(int(a/10)))

a = 1234
print(SOD(a))
