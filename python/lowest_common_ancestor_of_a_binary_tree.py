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
        return self.dfs(root, p, q)

    def dfs(
        self, node: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if node is None:
            return None
        left: Optional[TreeNode] = self.dfs(node.left, p, q)
        right: Optional[TreeNode] = self.dfs(node.right, p, q)
        if node == p or node == q:
            return node
        if left is not None and right is not None:
            return node
        return left if left is not None else right
