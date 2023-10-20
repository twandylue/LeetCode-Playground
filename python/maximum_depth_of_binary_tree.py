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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], count: int) -> int:
        if root is None:
            return count
        count += 1
        l: int = self.dfs(root.left, count)
        r: int = self.dfs(root.right, count)
        return max(l, r)


def test_maxDepth_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 9, 20, None, None, 15, 7])
    if root == None:
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
    if root == None:
        raise Exception("failed")

    expected: int = 2

    # act
    solution = Solution()
    actual = solution.maxDepth(root)

    # assert
    assert actual == expected
