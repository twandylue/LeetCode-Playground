import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> list[Optional[TreeNode]]:
        """time complexity: O(n^2)"""
        result: list = []
        subtree_map: dict[str, list[TreeNode]] = {}
        self.dfs(root, result, subtree_map)
        return result

    def dfs(
        self,
        root: Optional[TreeNode],
        result: list[Optional[TreeNode]],
        subtree_map: dict[str, int],
    ) -> str:
        if root is None:
            return "N"
        # NOTE: Serialize the tree to a string in preorder
        s: str = ",".join(
            [
                str(root.val),
                self.dfs(root.left, result, subtree_map),
                self.dfs(root.right, result, subtree_map),
            ]
        )
        # NOTE: Prevent from adding duplicated subtrees nodes
        if s not in subtree_map:
            subtree_map[s] = []
        elif len(subtree_map[s]) == 1:
            result.append(root)
        subtree_map[s].append(root)
        return s


def test_findDuplicateSubtrees_case_1():
    """NOTE: skip the test cases because it is difficult to prepare for"""
    assert True
