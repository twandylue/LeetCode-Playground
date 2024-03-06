import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from assert_two_tree import isSameTree
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


# Definiton for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """time complexity: O(n)"""
        result: list[int] = [float("inf")]
        prev: list[int] = [-1]
        self.dfs(root, prev, result)
        return result[0]

    def dfs(self, root: Optional[TreeNode], prev: list[int], result: list[int]) -> None:
        """dfs in inorder traversal"""
        if root is None:
            return
        self.dfs(root.left, prev, result)
        if prev[0] != -1:
            result[0] = min(result[0], root.val - prev[0])
        prev[0] = root.val
        self.dfs(root.right, prev, result)

    # NOTE: also works
    # def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    #     """time complexity: O(n)"""
    #     result: list[int] = []
    #     self.dfs(root, result)
    #     min_diff: int = float("inf")
    #     for i in range(len(result) - 1):
    #         min_diff = min(min_diff, result[i + 1] - result[i])
    #     return min_diff
    #
    # def dfs(self, root: Optional[TreeNode], result: list[int]) -> None:
    #     """dfs in inorder traversal"""
    #     if root is None:
    #         return
    #     self.dfs(root.left, result)
    #     result.append(root.val)
    #     self.dfs(root.right, result)


def test_minDiffInBST_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([4, 2, 6, 1, 3])
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minDiffInBST(root)

    # assert
    assert expected == actual


def test_minDiffInBST_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 0, 48, None, None, 12, 49])
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minDiffInBST(root)

    # assert
    assert expected == actual


def test_minDiffInBST_case_3():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([90, 69, None, 49, 89, None, 52])
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minDiffInBST(root)

    # assert
    assert expected == actual


def test_minDiffInBST_case_4():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList(
        [27, None, 34, None, 58, 50, None, 44]
    )
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.minDiffInBST(root)

    # assert
    assert expected == actual


def test_minDiffInBST_case_5():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList(
        [56, 42, 77, 23, 51, 75, 90, None, None, None, None, 67, None, 78, 99]
    )
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minDiffInBST(root)

    # assert
    assert expected == actual
