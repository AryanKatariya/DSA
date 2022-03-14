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

def buildTreePostIn(postorder, inorder):
    if inorder:
            root = Node(postorder.pop())
            ind = inorder.index(root.data)
            root.right = buildTreePostIn(inorder[ind+1:],postorder)
            root.left = buildTreePostIn(inorder[:ind],postorder)
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


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

root = buildTreePostIn(postorder, inorder)

printLevelATNewLine(root)
