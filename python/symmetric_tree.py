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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """time complexity: O(n)"""
        if root is None:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """dfs in preorder"""
        if left is None and right is None:
            return True
        if left is not None and right is None:
            return False
        if left is None and right is not None:
            return False
        if left.val != right.val:
            return False

        # NOTE:
        # This is pretty similar to the problem of same tree. However, the difference is that we need to compare
        # left.left and right.right, and left.right and right.left because the tree should be symmetric (mirror).
        return self.dfs(left.left, right.right) and self.dfs(right.left, left.right)


def test_isSymmetric_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 2, 3, 4, 4, 3])
    if root is None:
        raise Exception("failed")
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isSymmetric(root)

    # assert
    assert expected == actual


def test_isSymmetric_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 2, None, 3, None, 3])
    if root is None:
        raise Exception("failed")
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isSymmetric(root)

    # assert
    assert expected == actual
