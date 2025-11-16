from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """time complexity: O(n), space complexity: O(1)"""
        l: int = 0
        result: int = 0
        freq_map: dict[str, int] = defaultdict(int)
        max_freq: int = 0
        for r in range(len(s)):
            freq_map[s[r]] += 1
            max_freq = max(max_freq, freq_map[s[r]])
            while r - l + 1 - max_freq > k:
                freq_map[s[l]] -= 1
                max_freq = max(max_freq, freq_map[s[r]])
                l += 1
            result = max(result, r - l + 1)
        return result


def test_characterReplacement_case_1():
    # arrange
    s: str = "ABAB"
    k: str = 2
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.characterReplacement(s, k)

    # assert
    assert expected == actual


def test_characterReplacement_case_2():
    # arrange
    s: str = "AABABBA"
    k: str = 1
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.characterReplacement(s, k)

    # assert
    assert expected == actual


def test_characterReplacement_case_3():
    # arrange
    s: str = "BAAA"
    k: str = 0
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.characterReplacement(s, k)

    # assert
    assert expected == actual


def test_characterReplacement_case_4():
    # arrange
    s: str = "ABBB"
    k: str = 2
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.characterReplacement(s, k)

    # assert
    assert expected == actual
