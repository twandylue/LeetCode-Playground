import sys

sys.path.append("../models")

from typing import Optional
from binary_tree_node import TreeNode


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """time complexity: O(n)"""
    return dfs(p, q)


def dfs(p: Optional[TreeNode], q: list[Optional[TreeNode]]) -> bool:
    """preorder traversal"""
    if p is None and q is None:
        return True

    if p is None and q is not None:
        return False

    if p is not None and q is None:
        return False

    if p.val != q.val:
        return False

    return dfs(p.right, q.right) and dfs(p.left, q.left)
