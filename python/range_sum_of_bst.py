import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """time complexity: O(n)"""
        if root is None:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )


def test_rangeSumBST_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([10, 5, 15, 3, 7, None, 18])
    low: int = 7
    high: int = 15
    expected: int = 32

    # act
    actual: int = Solution().rangeSumBST(root, low, high)

    # assert
    assert expected == actual


def test_rangeSumBST_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList(
        [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
    )
    low: int = 6
    high: int = 10
    expected: int = 23

    # act
    actual: int = Solution().rangeSumBST(root, low, high)

    # assert
    assert expected == actual
