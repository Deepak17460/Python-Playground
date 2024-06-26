# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorderTraversal(node):
            if node:
                inorderTraversal(node.left)
                nodes.append(node.val)
                inorderTraversal(node.right)
        inorderTraversal(root)
        def buildBalancedBST(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nodes[mid])
            node.left = buildBalancedBST(start, mid - 1)
            node.right = buildBalancedBST(mid + 1, end)
            return node
        return buildBalancedBST(0, len(nodes) - 1)
