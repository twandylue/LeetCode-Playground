class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """time complexity: O(n * 2^n)"""
        result: list[list[str]] = []
        subset: list[str] = []
        self.bfs(0, subset, result, s)

        return result

    def bfs(self, pos: int, subset: list[str], result: list[list[str]], s: str) -> None:
        if pos >= len(s):
            result.append(subset[:])
            return None

        for i in range(pos, len(s)):
            if not self.isPali(pos, i, s):
                continue
            subset.append(s[pos : i + 1])
            self.bfs(i + 1, subset, result, s)
            subset.pop()

    def isPali(self, l: int, r: int, s: str) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            if r > 0:
                r -= 1

        return True


def test_partition_case_1():
    # arrange
    s: str = "aab"
    expected: list[list[str]] = [["a", "a", "b"], ["aa", "b"]]

    # act
    solution = Solution()
    actual = solution.partition(s)

    # assert
    assert expected == actual


def test_partition_case_2():
    # arrange
    s: str = "a"
    expected: list[list[str]] = [["a"]]

    # act
    solution = Solution()
    actual = solution.partition(s)

    # assert
    assert expected == actual
