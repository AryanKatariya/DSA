class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def printNodesWithoutSibling(root) :
    if root is None:
        return 0
    if root.left is None and root.right is not None:
        print(root.right.data, end=' ')
    elif root.left is not None and root.right is None:
        print(root.left.data, end=' ')

    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(5)



btn1.left = btn2
btn1.right = btn3
btn2.left = btn4


print(printNodesWithoutSibling(btn1))
