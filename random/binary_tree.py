class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    # Base case: if root is null, or we found either p or q
    if not root or root == p or root == q:
        return root
        
    # Search left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    # If both left and right returned a node, this root is the LCA
    if left and right:
        return root
        
    # Otherwise, return the non-null child
    return left if left else right

class Tree2:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    