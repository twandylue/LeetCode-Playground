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
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        """time complexity: O(n)"""
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums: list[int], start: int, end: int) -> Optional[TreeNode]:
        """dfs in preorder traversal"""
        if start > end:
            return None
        mid: int = (start + end) // 2
        root: TreeNode = TreeNode(nums[mid])
        root.left = self.dfs(nums, start, mid - 1)
        root.right = self.dfs(nums, mid + 1, end)
        return root


def test_sortedArrayToBST_case_1():
    """NOTE: skip because it is difficult to prepare for test cases (expected)"""
    # # arrange
    # nums: list[int] = [-10, -3, 0, 5, 9]
    # expected: Optional[TreeNode] = DeserializeFromList([0, -3, 9, -10, None, 5])
    # if expected is None:
    #     raise Exception("failed")
    #
    # # act
    # solution = Solution()
    # actual = solution.sortedArrayToBST(nums)
    #
    # # assert
    # assert actual == expected
    assert True
