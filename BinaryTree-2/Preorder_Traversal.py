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

def preorderTraversal(root):
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.data)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    result.append(curr.data)
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right

        return result

root = levelWiseInput()
print(preorderTraversal(root))
