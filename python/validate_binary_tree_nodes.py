class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: list[int], rightChild: list[int]
    ) -> bool:
        """time complexity: O(n)"""
        hasParent: set[int] = set(leftChild + rightChild)
        hasParent.discard(-1)
        if len(hasParent) == n:
            return False
        root: int = -1
        for i in range(n):
            if i not in hasParent:
                root = i
        visited: set[int] = set()
        return self.dfs(root, leftChild, rightChild, visited) and len(visited) == n

    def dfs(
        self, i: int, leftChild: list[int], rightChild: list[int], visited: set[int]
    ) -> bool:
        if i == -1:
            return True
        if i in visited:
            return False
        visited.add(i)
        return self.dfs(leftChild[i], leftChild, rightChild, visited) and self.dfs(
            rightChild[i], leftChild, rightChild, visited
        )


def test_validateBinaryTreeNodes_case_1():
    # arrange
    n: int = 4
    leftChild: list[int] = [1, -1, 3, -1]
    rightChild: list[int] = [2, -1, -1, -1]
    expected: bool = True

    # act
    actual: bool = Solution().validateBinaryTreeNodes(n, leftChild, rightChild)

    # assert
    assert expected == actual


def test_validateBinaryTreeNodes_case_2():
    # arrange
    n: int = 4
    leftChild: list[int] = [1, -1, 3, -1]
    rightChild: list[int] = [2, 3, -1, -1]
    expected: bool = False

    # act
    actual: bool = Solution().validateBinaryTreeNodes(n, leftChild, rightChild)

    # assert
    assert expected == actual


def test_validateBinaryTreeNodes_case_3():
    # arrange
    n: int = 2
    leftChild: list[int] = [1, 0]
    rightChild: list[int] = [-1, -1]
    expected: bool = False

    # act
    actual: bool = Solution().validateBinaryTreeNodes(n, leftChild, rightChild)

    # assert
    assert expected == actual
