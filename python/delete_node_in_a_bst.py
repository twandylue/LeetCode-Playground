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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """time complexity: O(log(n)) = O(h)"""
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            ## NOTE: This is not necessary because this is a BST
            # if root.left is None:
            #     return root.right
            if root.right is None:
                return root.left
            curr = root.right
            while curr.left is not None:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root


def test_deleteNode_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([5, 3, 6, 2, 4, None, 7])
    key: int = 3
    expected: Optional[int] = [5, 4, 6, 2, None, None, 7]

    # act
    solution = Solution()
    actual = solution.deleteNode(root, key)

    # assert
    assert expected == SerializeBinaryTreeToList(actual)


def test_deleteNode_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([5, 3, 6, 2, 4, None, 7])
    key: int = 0
    expected: Optional[int] = [5, 3, 6, 2, 4, None, 7]

    # act
    solution = Solution()
    actual = solution.deleteNode(root, key)

    # assert
    assert expected == SerializeBinaryTreeToList(actual)


def test_deleteNode_case_3():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([])
    key: int = 0
    expected: Optional[int] = []

    # act
    solution = Solution()
    actual = solution.deleteNode(root, key)

    # assert
    assert expected == SerializeBinaryTreeToList(actual)
