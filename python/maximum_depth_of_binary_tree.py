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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """time complexity: O(n)"""
        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> int:
        """postorder traversal"""
        if root is None:
            return 0
        left: int = self.dfs(root.left)
        right: int = self.dfs(root.right)
        return 1 + max(left, right)


def test_maxDepth_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 9, 20, None, None, 15, 7])
    if root is None:
        raise Exception("failed")
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.maxDepth(root)

    # assert
    assert actual == expected


def test_maxDepth_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, None, 2])
    if root is None:
        raise Exception("failed")
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.maxDepth(root)

    # assert
    assert actual == expected
