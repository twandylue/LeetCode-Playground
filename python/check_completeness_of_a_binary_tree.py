import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """time complexity: O(n)"""
        if root is None:
            return True

        que: deque[Optional[TreeNode]] = deque()
        que.append(root)
        while len(que) > 0:
            node: Optional[TreeNode] = que.popleft()
            if node is None:
                break
            que.append(node.left)
            que.append(node.right)
        while len(que) > 0:
            if que.popleft() is not None:
                return False
        return True


def test_isCompleteTree_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 3, 4, 5, 6])
    if root is None:
        raise Exception("failed")
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isCompleteTree(root)

    # assert
    assert expected == actual


def test_isCompleteTree_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 3, 4, 5, None, 7])
    if root is None:
        raise Exception("failed")
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isCompleteTree(root)

    # assert
    assert expected == actual
