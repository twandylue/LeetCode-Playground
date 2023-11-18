from collections import deque
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        queue: deque[tuple[TreeNode, str]] = deque()
        queue.append((root, str(root.val)))
        paths: list[str] = list()

        while len(queue) > 0:
            node, path = queue.popleft()
            if node.left == None and node.right == None:
                paths.append(path)
                continue
            if node.left != None:
                queue.append((node.left, path + "->" + str(node.left.val)))
            if node.right != None:
                queue.append((node.right, path + "->" + str(node.right.val)))

        return paths


def test_binaryTreePaths_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1, 2, 3, None, 5])
    if root == None:
        raise Exception("failed")
    expected: list[str] = ["1->2->5", "1->3"]

    # act
    solution = Solution()
    actual = solution.binaryTreePaths(root)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_binaryTreePaths_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1])
    if root == None:
        raise Exception("failed")
    expected: list[str] = ["1"]

    # act
    solution = Solution()
    actual = solution.binaryTreePaths(root)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
