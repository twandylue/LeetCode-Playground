import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


def maxDepth(self, root: Optional[TreeNode]) -> int:
    """time complexity: O(n)"""
    if root is None:
        return 0
    return self.dfs(root)


def dfs(self, root: Optional[TreeNode]) -> int:
    """postorder traversal"""
    if root is None:
        return 0
    left: int = self.dfs(root.left)
    right: int = self.dfs(root.right)
    return 1 + max(left, right)
