from typing import Optional, Tuple
import sys

sys.path.append("./models")
from binary_tree_node import TreeNode

sys.path.append("./utils")
from deserialize_to_binary_tree import DeserializeFromList


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]

    def helper(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
        if root == None:
            return (True, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return (balanced, max(left[1], right[1]) + 1)


def test_isBalanced_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 9, 20, None, None, 15, 7])
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isBalanced(root)

    # assert
    assert expected == actual


def test_isBalanced_case_2():
    # arrange
    arr: list[Optional[int]] = [1, 2, 2, 3, 3, None, None, 4, 4]
    root: Optional[TreeNode] = DeserializeFromList(arr)
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isBalanced(root)

    # assert
    assert expected == actual


def test_isBalanced_case_3():
    # arrange
    root: Optional[TreeNode] = None
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isBalanced(root)

    # assert
    assert expected == actual
