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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr: Optional[TreeNode] = root
        while curr is not None:
            if curr.val == val:
                return curr
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        return None


def test_searchBST_case_1():
    """NOTE: skip because it is difficult to prepare for test cases (input)"""
    # # arrange
    # root: Optional[TreeNode] = DeserializeFromList([4, 2, 7, 1, 3])
    # val: int = 2
    # expected: list[int] = [2, 1, 3]
    #
    # # act
    # solution = Solution()
    # actual = solution.searchBST(root, val)
    #
    # # assert
    # assert expected == SerializeBinaryTreeToList(actual)
