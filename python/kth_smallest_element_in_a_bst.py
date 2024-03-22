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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """time complexity: O(n)"""
        arr: list[int] = []
        self.dfs(root, arr)
        return arr[k - 1]

    def dfs(self, node: Optional[TreeNode], arr: list[int]) -> None:
        """dfs in inorder traversal"""
        if node is None:
            return
        self.dfs(node.left, arr)
        arr.append(node.val)
        self.dfs(node.right, arr)


def test_kthSmallest_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 1, 4, None, 2])
    if root == None:
        raise Exception("failed")
    k: int = 1
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.kthSmallest(root, k)

    # assert
    assert actual == expected


def test_kthSmallest_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([5, 3, 6, 2, 4, None, None, 1])
    if root == None:
        raise Exception("failed")
    k: int = 3
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.kthSmallest(root, k)

    # assert
    assert actual == expected
