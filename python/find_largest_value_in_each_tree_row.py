import sys
from collections import deque

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
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        """time complexity: O(n)"""
        if root is None:
            return []
        queue: deque[TreeNode] = deque([root])
        result: list[int] = []
        while len(queue) > 0:
            length: int = len(queue)
            max_num: float = queue[0].val
            for _ in range(length):
                node = queue.popleft()
                max_num = max(node.val, max_num)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(max_num)

        return result


def test_largestValues_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 3, 2, 5, 3, None, 9])
    expected: list[int] = [1, 3, 9]

    # act
    actual: list[int] = Solution().largestValues(root)

    # assert
    assert expected == actual


def test_largestValues_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 3])
    expected: list[int] = [1, 3]

    # act
    actual: list[int] = Solution().largestValues(root)

    # assert
    assert expected == actual
