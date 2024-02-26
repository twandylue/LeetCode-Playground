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
        if root is None:
            return 0
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], depth: int) -> int:
        """postorder traversal"""
        if root is None:
            return depth
        l: int = self.dfs(root.left, depth + 1)
        r: int = self.dfs(root.right, depth + 1)
        return max(l, r)


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
