from collections import deque
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        return self.dfs(root, 0, targetSum)

    def dfs(self, root: Optional[TreeNode], accu: int, targetSum: int) -> bool:
        if root == None:
            return False

        if root.left == None and root.right == None and accu + root.val == targetSum:
            return True

        if root.left == None and root.right == None and accu + root.val != targetSum:
            return False

        return self.dfs(root.left, accu + root.val, targetSum) or self.dfs(
            root.right, accu + root.val, targetSum
        )


def test_hasPathSum_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    )
    if root == None:
        raise Exception("failed")
    targetSum: int = 22
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.hasPathSum(root, targetSum)

    # assert
    assert expected == actual


def test_hasPathSum_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 3])
    if root == None:
        raise Exception("failed")
    targetSum: int = 5
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.hasPathSum(root, targetSum)

    # assert
    assert expected == actual


def test_hasPathSum_case_3():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([])
    targetSum: int = 0
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.hasPathSum(root, targetSum)

    # assert
    assert expected == actual
