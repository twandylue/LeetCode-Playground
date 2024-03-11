from typing import Optional
import sys

sys.path.append("./models")
from binary_tree_node import TreeNode

sys.path.append("./utils")
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """time complexity: O(n)"""
        result: list[int] = []
        self.dfs(root, result)
        return result

    def dfs(self, root: Optional[TreeNode], result) -> None:
        """dfs in preorder"""
        if root is None:
            return
        self.dfs(root.left, result)
        self.dfs(root.right, result)
        result.append(root.val)


def test_postorderTraversal_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, None, 2, 3])
    expected: list[int] = [3, 2, 1]

    # act
    solution = Solution()
    actual = solution.postorderTraversal(root)

    # assert
    assert expected == actual


def test_postorderTraversal_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([])
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.postorderTraversal(root)

    # assert
    assert expected == actual


def test_postorderTraversal_case_3():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1])
    expected: list[int] = [1]

    # act
    solution = Solution()
    actual = solution.postorderTraversal(root)

    # assert
    assert expected == actual
