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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """time complexity: O(n), space complexity: O(n), this is a bfs solution"""
        if root is None:
            return []
        result: list[list[int]] = []
        que: deque[Optional[TreeNode]] = deque([root])
        is_even: bool = True
        while len(que) > 0:
            level_size: int = len(que)
            level_vec: list[int] = []
            for _ in range(level_size):
                node: Optional[TreeNode] = que.popleft()
                if node is None:
                    continue
                level_vec.append(node.val)
                que.append(node.left)
                que.append(node.right)
            if not is_even:
                level_vec.reverse()
            is_even = not is_even
            if len(level_vec) > 0:
                result.append(level_vec)
        return result


def test_zigzagLevelOrder_case_1():
    "This is a test case"
    # arrange
    root: list[Optional[int]] = DeserializeFromList([3, 9, 20, None, None, 15, 7])
    expected: list[list[int]] = [[3], [20, 9], [15, 7]]

    # act
    solution = Solution()
    actual = solution.zigzagLevelOrder(root)

    # assert
    assert expected == actual


def test_zigzagLevelOrder_case_2():
    "This is a test case"
    # arrange
    root: list[Optional[int]] = DeserializeFromList([1])
    expected: list[list[int]] = [[1]]

    # act
    solution = Solution()
    actual = solution.zigzagLevelOrder(root)

    # assert
    assert expected == actual
