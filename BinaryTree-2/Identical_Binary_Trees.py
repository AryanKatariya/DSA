def _isSameTree(A, B):
        s = int(not A) + int(not B)
        if s == 2:
            return 1
        elif s == 1:
            return 0
        else:
            return _isSameTree(A.left, B.left) and _isSameTree(A.right, B.right) and A.val == B.val

def isSameTree(A, B):
	return int(_isSameTree(A, B))
