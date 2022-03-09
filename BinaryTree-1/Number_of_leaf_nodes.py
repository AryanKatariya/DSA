class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def numLeaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    numLeafleft = numLeaf(root.left)
    numLeafright = numLeaf(root.right)
    return numLeafleft + numLeafright

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

print(numLeaf(btn1))
