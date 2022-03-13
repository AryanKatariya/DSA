class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
def findMax(root):

    if (root == None):
        return INT_MIN
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res

def findMin(root):
    if (root == None):
        return INT_MAX

    res = root.data
    lres = findMin(root.left)
    rres = findMin(root.right)
    if (lres < res):
        res = lres
    if (rres < res):
        res = rres

    return res


def minMax(root):
    min = findMin(root)
    max = findMax(root)

    return min, max
