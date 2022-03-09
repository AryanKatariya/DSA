class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def countNodesGreaterThanX(root, x) :
    if root == None:
        return 0
    leftLargest = countNodesGreaterThanX(root.left,x)
    rightLargest = countNodesGreaterThanX(root.right,x)

    if root.data > x:
        return 1 + leftLargest + rightLargest
    return leftLargest + rightLargest

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

print(countNodesGreaterThanX(btn1,3))
