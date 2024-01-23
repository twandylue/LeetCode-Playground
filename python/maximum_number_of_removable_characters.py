class Solution:
    # NOTE: time complexity: O(nlogk)
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        l: int = 0
        r: int = len(removable) - 1
        result: int = 0
        while l <= r:
            mid: int = (l + r) // 2
            removed: set[int] = set(removable[: mid + 1])
            if self.isSubsequence(p, s, removed):
                result = max(mid + 1, result)
                l = mid + 1
            else:
                r = mid - 1

        return result

    def isSubsequence(self, subsequence: str, s: str, removed: set[int]) -> bool:
        i: int = 0
        j: int = 0
        while i < len(subsequence) and j < len(s):
            if j in removed or subsequence[i] != s[j]:
                j += 1
                continue
            i += 1
            j += 1

        return i == len(subsequence)


def test_maximumRemovals_case_1():
    # arrange
    s: str = "abcacb"
    p: str = "ab"
    removable: list[int] = [3, 1, 0]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.maximumRemovals(s, p, removable)

    # assert
    assert expected == actual


def test_maximumRemovals_case_2():
    # arrange
    s: str = "abcbddddd"
    p: str = "abcd"
    removable: list[int] = [3, 2, 1, 4, 5, 6]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.maximumRemovals(s, p, removable)

    # assert
    assert expected == actual


def test_maximumRemovals_case_3():
    # arrange
    s: str = "abcab"
    p: str = "abc"
    removable: list[int] = [0, 1, 2, 3, 4]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.maximumRemovals(s, p, removable)

    # assert
    assert expected == actual
