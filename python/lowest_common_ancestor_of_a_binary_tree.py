import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from assert_two_tree import isSameTree
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        "time complexity: O(n)"
        if root is None or root == p or root == q:
            return root
        left: Optional[TreeNode] = self.lowestCommonAncestor(root.left, p, q)
        right: Optional[TreeNode] = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        return left if left is not None else right
