class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def changeToDepthTree(root,level=0):
    if root is None:
        return
    if root.data is not None:
        root.data = level
    left = changeToDepthTree(root.left, level + 1)
    right = changeToDepthTree(root.right, level + 1)

def PrintTree(root):
    if root == None:
        return
    print(root.data, end=':')

    if root.left != None:
        print('L',root.left.data,end=',')

    if root.right != None:
        print('R',root.right.data,end='')

    print()

    PrintTree(root.left)
    PrintTree(root.right)

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

PrintTree(btn1)
print(changeToDepthTree(btn1))
print()
PrintTree(btn1)
