# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        "time complexity: O(n)"
        visited: set[TreeNode] = set()
        result: TreeNode = None
        while p is not None:
            visited.add(p)
            p = p.parent
        while q is not None:
            if q in visited:
                result = q
                break
            visited.add(q)
            q = q.parent
        return result
