class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def search(root, x):
    if root is None:
        return None
    if x == root.data:
        return root
    if x < root.data:
        return search(root.left, x)
    if x > root.data:
        return search(root.right, x)
