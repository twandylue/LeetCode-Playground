import sys

sys.path.append("./models")
sys.path.append("./utils")

from collections import deque
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return -1
        l: int = root.left.val
        r: int = root.right.val
        if root.left.val == root.val:
            l = self.findSecondMinimumValue(root.left)
        if root.right.val == root.val:
            r = self.findSecondMinimumValue(root.right)
        if l != -1 and r != -1:
            return min(l, r)
        elif r != -1:
            return r
        else:
            return l


def test_findSecondMinimumValue_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([2, 2, 5, None, None, 5, 7])
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.findSecondMinimumValue(root)

    # assert
    assert actual == expected


def test_findSecondMinimumValue_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([2, 2, 2])
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.findSecondMinimumValue(root)

    # assert
    assert actual == expected
