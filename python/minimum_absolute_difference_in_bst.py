import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from assert_two_tree import isSameTree
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
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


def test_getMinimumDifference_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([4, 2, 6, 1, 3])
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.getMinimumDifference(root)

    # assert
    assert expected == actual
