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

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

print(height(btn1))
