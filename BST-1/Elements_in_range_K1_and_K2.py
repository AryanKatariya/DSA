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

def elementsInRangeK1K2(root, k1, k2):
    if root is None:
        return None

    elementsInRangeK1K2(root.left, k1, k2)

    if root.data >= k1 and root.data <= k2:
        print(root.data, end = " ")

    elementsInRangeK1K2(root.right, k1, k2)

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

root = levelWiseInput()
printLevelATNewLine(root)
print(elementsInRangeK1K2(root,1,5))
