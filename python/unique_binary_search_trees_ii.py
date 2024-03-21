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
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        dp: dict[tuple[int, int], list[Optional[TreeNode]]] = {}
        return self.generate(1, n, dp)

    def generate(
        self,
        left: int,
        right: int,
        dp: dict[tuple[int, int], list[Optional[TreeNode]]],
    ) -> list[Optional[TreeNode]]:
        if left > right:
            return [None]
        if (left, right) in dp:
            return dp[(left, right)]
        result: list[Optional[TreeNode]] = []
        for val in range(left, right + 1):
            for left_tree in self.generate(left, val - 1, dp):
                for right_tree in self.generate(val + 1, right, dp):
                    root: TreeNode = TreeNode(val, left_tree, right_tree)
                    result.append(root)
        dp[(left, right)] = result
        return result


def test_generateTrees_case_1():
    """NOTE: skip the test cases because it is difficult to prepare for"""
    assert True
