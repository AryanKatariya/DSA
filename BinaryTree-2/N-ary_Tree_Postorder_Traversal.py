def postorder(root):
        postorder = []
        traverse(root, postorder)
        return postorder

def traverse(root, postorder):
    if not root:
        return
    for child in root.children:
        traverse(child, postorder)
    postorder.append(root.val)
