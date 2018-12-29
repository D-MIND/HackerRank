def check(root, mymin, mymax):
    if root == None:
        return True
    if root.data <= mymin or root.data >= mymax:
        return False
    return check(root.left, mymin, root.data) and check(root.right, root.data, mymax)

def checkBST(root):
    return check(root, float('-inf'), float('inf'))
