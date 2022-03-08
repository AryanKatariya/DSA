class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def isNodePresent(root, x) :
    if root == None:
        return
    if root.data == x:
        return True
    left = isNodePresent(root.left, x)
    right = isNodePresent(root.right, x)

    if left:
        return True
    if right:
        return True

btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

if isNodePresent(btn1,6) :
	print("True")

else :
	print("False")
