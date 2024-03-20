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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """time complexity: O(n)"""
        result: int = 0
        que: deque[tuple[Optional[TreeNode], int, int]] = deque()
        que.append((root, 1, 0))
        prev_level: int = 0
        prev_num: int = 1
        while len(que) > 0:
            node, num, level = que.popleft()
            if node is not None:
                if level > prev_level:
                    prev_level = level
                    prev_num = num
                result = max(result, num - prev_num + 1)
                que.append((node.left, num * 2, level + 1))
                que.append((node.right, num * 2 + 1, level + 1))
        return result


def test_widthOfBinaryTree_case_1():
    """This is a test case"""
    # arrange
    root: TreeNode = DeserializeFromList([1, 3, 2, 5, 3, None, 9])
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.widthOfBinaryTree(root)

    # assert
    assert expected == actual


def test_widthOfBinaryTree_case_2():
    """This is a test case"""
    # arrange
    root: TreeNode = DeserializeFromList([1, 3, 2, 5, None, None, 9, 6, None, 7])
    expected: int = 7

    # act
    solution = Solution()
    actual = solution.widthOfBinaryTree(root)

    # assert
    assert expected == actual


def test_widthOfBinaryTree_case_3():
    """This is a test case"""
    # arrange
    root: TreeNode = DeserializeFromList([1, 3, 2, 5])
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.widthOfBinaryTree(root)

    # assert
    assert expected == actual
