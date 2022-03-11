class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)

    if left > right:
        return 1 + left
    return 1 + right

def getHeightAndCheckBalanced(root):
    if root == None:
        return 0, True

    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)

    h = 1 + max(lh, rh)

    if lh - rh > 1 or rh - lh > 1:
        return h, False

    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False

def isBalanced2(root):
    h, isRootBalanced = getHeightAndCheckBalanced(root)
    return isRootBalanced

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
