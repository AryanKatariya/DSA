'''Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.'''

def addDigits(num):
        def addDigits(self, num: int) -> int:
            while num > 9:
                num = num//10 + num%10
            return num

num = 38
print(num//10)
print(num%10)
while num > 9:
    num = num//10 + num%10
    print(num)
