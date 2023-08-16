from typing import Optional
import sys

sys.path.append("./models")
from binary_tree_node import TreeNode

sys.path.append("./utils")
from deserialize_to_binary_tree import DeserializeFromList


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root != None:
            return self.dfs(root.val, root)
        else:
            return 0

    def dfs(self, maxVal: int, node: TreeNode) -> int:
        count: int = 0
        if node != None:
            if node.val >= maxVal:
                count += 1
            maxVal = max(maxVal, node.val)
            count += self.dfs(maxVal, node.left)
            count += self.dfs(maxVal, node.right)

            return count
        else:
            return 0


def test_goodNodes_case_1():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 1, 4, 3, None, 1, 5])
    expected: int = 4

    # act
    actual: int = Solution().goodNodes(root)

    # assert
    assert actual == expected


def test_goodNodes_case_2():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([1])
    expected: int = 1

    # act
    actual: int = Solution().goodNodes(root)

    # assert
    assert actual == expected


def test_goodNodes_case_3():
    # arrange
    root: Optional[TreeNode] = DeserializeFromList([3, 3, None, 4, 2])
    expected: int = 3

    # act
    actual: int = Solution().goodNodes(root)

    # assert
    assert actual == expected
