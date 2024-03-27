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
    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        """time complexity: O(2^n)"""
        dp: dict[int, list[Optional[TreeNode]]] = {0: [], 1: [TreeNode(0, None, None)]}
        return self.backtrack(n, dp)

    def backtrack(
        self, n: int, dp: dict[int, list[Optional[TreeNode]]]
    ) -> list[Optional[TreeNode]]:
        """backtracking"""
        if n in dp:
            return dp[n]
        result: list[Optional[TreeNode]] = []
        for l in range(n):
            r: int = n - 1 - l
            left_trees: list[Optional[TreeNode]] = self.backtrack(l, dp)
            right_trees: list[Optional[TreeNode]] = self.backtrack(r, dp)
            for t1 in left_trees:
                for t2 in right_trees:
                    result.append(TreeNode(0, t1, t2))
        dp[n] = result
        return result


def test_allPossibleFBT_case_1():
    """NOTE: skip because it is difficult to prepare for test cases (input)"""
    assert True
