class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def printDepthK(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left, k-1)
    printDepthK(root.right, k-1)

def printDepthKV2(root,k,d=0):
    if root is None:
        return
    if k == d:
        print(root.data)
        return
    printDepthKV2(root.left, k,d+1)
    printDepthKV2(root.right, k,d+1)

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

print(printDepthK(btn1,2))
print()
print(printDepthKV2(btn1,2))
