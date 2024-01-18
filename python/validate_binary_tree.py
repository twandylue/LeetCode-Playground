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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -float("inf"), float("inf"))

    def isValid(self, root: Optional[TreeNode], minNumber: int, maxNumber: int) -> bool:
        if root == None:
            return True

        if root.val <= minNumber or root.val >= maxNumber:
            return False

        return self.isValid(root.left, minNumber, root.val) and self.isValid(
            root.right, root.val, maxNumber
        )


def test_isValidBST_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([2, 1, 3])
    if root == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isValidBST(root)

    # assert
    assert actual == True


def test_isValidBST_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([5, 1, 4, None, None, 3, 6])
    if root == None:
        raise Exception("failed")

    # act
    solution = Solution()
    actual = solution.isValidBST(root)

    # assert
    assert actual == False
