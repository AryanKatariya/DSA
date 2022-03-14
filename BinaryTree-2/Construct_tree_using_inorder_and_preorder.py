import queue

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

def buildTreePreIn(preorder, inorder):
    if len(preorder) == 0:
        return None

    rootData = preorder[0]
    root = Node(rootData)
    rootIndexInorder = -1

    for i in range(0,len(inorder)):
        if inorder[i] == rootData:
            rootIndexInorder = i
            break
    if rootIndexInorder == -1:
        return None

    leftInorder = inorder[0:rootIndexInorder]
    rightInorder = inorder[rootIndexInorder + 1:]

    x = len(leftInorder)

    leftPreorder = preorder[1:1+x]
    rightPreorder = preorder[1+x:]

    root.left = buildTreePreIn(leftPreorder, leftInorder)
    root.right = buildTreePreIn(rightPreorder, rightInorder)

    return root

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


inorder = [4,2,5,1,6,3,7]
preorder = [1,2,4,5,3,6,7]

root = buildTreePreIn(preorder, inorder)

printLevelATNewLine(root)
