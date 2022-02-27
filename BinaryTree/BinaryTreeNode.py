class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data


btn1 = Node(1)
btn2 = Node(4)
btn3 = Node(3)

btn1.left = btn2
btn1.right = btn3
