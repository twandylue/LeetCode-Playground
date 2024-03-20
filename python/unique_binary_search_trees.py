class Solution:
    def numTrees(self, n: int) -> int:
        """time complexity: O(n^2)"""
        num_trees: list[int] = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total: int = 0
            for root in range(1, nodes + 1):
                left: int = root - 1
                right: int = nodes - root
                total += num_trees[left] * num_trees[right]
            num_trees[nodes] = total
        return num_trees[n]


def test_numTrees_case_1():
    """This is a test case"""
    # arrange
    n: int = 3
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.numTrees(n)

    # assert
    assert expected == actual


def test_numTrees_case_2():
    """This is a test case"""
    # arrange
    n: int = 1
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.numTrees(n)

    # assert
    assert expected == actual
