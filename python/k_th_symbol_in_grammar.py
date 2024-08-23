class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """time complexity: O(n)"""
        curr: int = 0
        left: int = 1
        right: int = 2 ** (n - 1)
        for _ in range(n - 1):
            mid: int = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                curr = 0 if curr == 1 else 1
        return curr


def test_kthGrammar_case_1():
    # arrange
    n: int = 1
    k: int = 1
    expected: int = 0

    # act
    actual: int = Solution().kthGrammar(n, k)

    # assert
    assert expected == actual


def test_kthGrammar_case_2():
    # arrange
    n: int = 2
    k: int = 1
    expected: int = 0

    # act
    actual: int = Solution().kthGrammar(n, k)

    # assert
    assert expected == actual


def test_kthGrammar_case_3():
    # arrange
    n: int = 2
    k: int = 2
    expected: int = 1

    # act
    actual: int = Solution().kthGrammar(n, k)

    # assert
    assert expected == actual
