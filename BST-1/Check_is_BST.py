import queue

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def levelWiseInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    q.put(root)

    while (not(q.empty())):
        current_node = q.get()

        print("Enter left child of ", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = Node(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        print("Enter right child of ", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild =  Node(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)


    return root

def minTree(root):
    if root == None:
        return 1000000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)

def maxTree(root):
    if root == None:
        return -10000000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.data)

def isBST(root):
    if root == None:
        return True
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    if root.data > rightMin or root.data <= leftMax:
        return False

    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)

    return isLeftBST and isRightBST

    return root

def isBST2(root):
    if root == None:
        return 1000000, -1000000, True
    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)

    isTreeBST = True

    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST = False

    return minimum, maximum, isTreeBST

def isBST3(root, min_range, max_range):
    if root == None:
        return True
    if root.data < min_range or root.data > max_range:
        return False

    isLeftWithinConstraints = isBST3(root.left, min_range, root.data -1)
    isRightWithinConstraints = isBST3(root.right, root.data, max_range)

    return isLeftWithinConstraints and isRightWithinConstraints

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

def printLevelATNewLine(root):
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ
