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
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode", nodes: list[int]
    ) -> "TreeNode":
        "time complexity: O(n)"
        nodes_set: set[int] = set()
        for node in nodes:
            nodes_set.add(node.val)
        return self.dfs(root, p, q, nodes_set)

    def dfs(
        self, node: TreeNode, p: TreeNode, q: TreeNode, nodes_set: set[int]
    ) -> TreeNode:
        if node is None or node.val in nodes_set:
            return node
        left: TreeNode = self.dfs(node.left, p, q, nodes_set)
        right: TreeNode = self.dfs(node.right, p, q, nodes_set)
        if left is not None and right is not None:
            return node
        return left if left is not None else right
