class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

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

def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    leftTree = tree()
    rightTree = tree()
    root.left = leftTree
    root.right = rightTree
    return root

def removeLeaves(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    removeLeaves(root.left)
    removeLeaves(root.right)

    return root

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
