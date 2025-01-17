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
        found_p: list[bool] = [False]
        found_q: list[bool] = [False]
        node: Optional[TreeNode] = self.dfs(root, p, q, found_p, found_q)
        return node if found_p[0] and found_q[0] else None

    def dfs(
        self,
        node: TreeNode,
        p: TreeNode,
        q: TreeNode,
        found_p: list[bool],
        found_q: list[bool],
    ) -> TreeNode:
        if node is None:
            return None
        left: Optional[TreeNode] = self.dfs(node.left, p, q, found_p, found_q)
        right: Optional[TreeNode] = self.dfs(node.right, p, q, found_p, found_q)
        if node == p:
            found_p[0] = True
            return node
        if node == q:
            found_q[0] = True
            return node
        if left is not None and right is not None:
            return node
        return left if left is not None else right
