import queue
def checkRedundancy(s):
    q = queue.LifoQueue()
    temp = 0
    l = len(s)
    for i in range(l-1):
        c = s[i]
        n = s[i+1]
        if (c == "(" and n == ")"):
            return True
        elif (c == "(" and n == ")"):
            temp = 2
        elif c == ")" and n == ")" and temp == 2:
            return True
        return False

s = input()
ans = checkRedundancy(s)
print(ans)
