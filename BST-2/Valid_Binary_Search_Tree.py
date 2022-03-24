def valid(node,left,right):
        if node is None:
            return True
        if not (node.val < right and node.val > left):
            return False
        return (valid(node.right, node.val, right) and
                valid(node.left, left, node.val))
