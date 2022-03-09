'''
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1'''

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data),
        printInorder(root.right)


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)


def printPreorder(root):
    if root:
        print(root.data),
        printPreorder(root.left)
        printPreorder(root.right)

def inorderTraversal(A):
    stack, ans = list(), list()
    if A:
        stack.append(A)

    while stack:
        node = stack[-1]
        if not node.left or hasattr(node.left, 'visited'):
            node.visited = True
            ans.append(stack.pop().data)

            if node.right:
                stack.append(node.right)
        else:
            stack.append(node.left)

    return ans

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

printInorder(btn1)
print()
printPreorder(btn1)
print()
printPostorder(btn1)
print()
print(inorderTraversal(btn1))
