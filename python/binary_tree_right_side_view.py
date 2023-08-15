from collections import deque
from typing import Deque, Optional
import sys

sys.path.append("./models")
from binary_tree_node import TreeNode

sys.path.append("./utils")
from deserialize_to_binary_tree import DeserializeFromList


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result: list[int] = []
        queue: Deque[Optional[TreeNode]] = deque([root])

        while len(queue) > 0:
            rightNode: Optional[TreeNode] = None
            queLen: int = len(queue)
            for _ in range(0, queLen):
                ele: Optional[TreeNode] = queue.popleft()
                if ele != None:
                    rightNode = ele
                    queue.append(ele.left)
                    queue.append(ele.right)

            if rightNode != None:
                result.append(rightNode.val)

        return result


def test_rightSideView_case_1():
    # arrange
    arr: list[Optional[int]] = [1, 2, 3, None, 5, None, 4]
    root: Optional[TreeNode] = DeserializeFromList(arr)
    expected: list[int] = [1, 3, 4]

    # act
    solution = Solution()
    actual = solution.rightSideView(root)

    # assert
    assert actual == expected


def test_rightSideView_case_2():
    # arrange
    arr: list[Optional[int]] = [1, None, 3]
    root: Optional[TreeNode] = DeserializeFromList(arr)
    expected: list[int] = [1, 3]

    # act
    solution = Solution()
    actual = solution.rightSideView(root)

    # assert
    assert actual == expected


def test_rightSideView_case_3():
    # arrange
    arr: list[Optional[int]] = []
    root: Optional[TreeNode] = DeserializeFromList(arr)
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.rightSideView(root)

    # assert
    assert actual == expected
