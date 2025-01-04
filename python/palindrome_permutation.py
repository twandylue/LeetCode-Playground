class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """time complexity: O(n)"""
        arr: list[int] = [0] * 52
        count_odd: int = 0
        for c in s:
            index: int = self.char_to_num(c)
            if index == -1:
                continue
            arr[index] += 1
            if arr[index] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1
        return count_odd <= 1

    def char_to_num(self, c: str) -> int:
        return ord(c) - ord("a") if c.isalpha() else -1


def test_canPermutePalindrome_case_1():
    # arrange
    s: str = "tactcoa"
    expected: bool = True

    # act
    actual = Solution().canPermutePalindrome(s)

    # assert
    assert expected == actual


def test_canPermutePalindrome_case_2():
    # arrange
    s: str = "AaBb//a"
    expected: bool = False

    # act
    actual = Solution().canPermutePalindrome(s)

    # assert
    assert expected == actual
