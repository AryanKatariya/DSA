'''Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234'''

def addToArrayForm(num,k):
        n = 0
        for a in num:
            n = n*10 + a
        n += k
        A = []
        while n > 0:
            A.append(n%10)
            n //= 10
        return A[::-1] if A else [0]
