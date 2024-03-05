import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from assert_two_tree import isSameTree
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
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """time complexity: O(n)"""
        if root is None:
            return []
        result: list[list[int]] = []
        queue: deque[TreeNode] = deque()
        queue.append(root)
        while len(queue) > 0:
            level_size: int = len(queue)
            level_vec: list[int] = []
            for _ in range(level_size):
                node: TreeNode = queue.popleft()
                if node is not None:
                    level_vec.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(level_vec) > 0:
                result.append(level_vec)
        return result


def test_levelOrder_case_1():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 9, 20, None, None, 15, 7])
    if root is None:
        raise Exception("failed")
    expected: list[list[int]] = [[3], [9, 20], [15, 7]]

    # act
    solution = Solution()
    actual = solution.levelOrder(root)

    # assert
    assert expected == actual


def test_levelOrder_case_2():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1])
    if root is None:
        raise Exception("failed")
    expected: list[list[int]] = [[1]]

    # act
    solution = Solution()
    actual = solution.levelOrder(root)

    # assert
    assert expected == actual


def test_levelOrder_case_3():
    """This is a test case"""
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([])
    expected: list[list[int]] = []

    # act
    solution = Solution()
    actual = solution.levelOrder(root)

    # assert
    assert expected == actual
