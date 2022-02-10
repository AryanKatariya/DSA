'''Reverse a stack using another stack'''

def reverseStack(stack1,stack2):
    if len(stack1) <= 1:
        return

    while len(stack1) != 1:
        ele = stack1.pop()
        stack2.append(ele)

    lastElement = stack1.pop()

    while len(stack2) != 0:
        ele = stack2.pop()
        stack1.append(ele)

    reverseStack(stack1,stack2)
    stack1.append(lastElement)

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1,s2)
while(len(s1) !=0):
    print(s1.pop(),end= ' ')
