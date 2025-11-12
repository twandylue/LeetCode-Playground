class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Time complexity: O(n)
        mask: int = 0
        result: int = 0
        prefix_map: dict[int, int] = {0: 1}
        for i, ch in enumerate(word):
            idx: int = ord(ch) - ord("a")
            mask ^= 1 << idx
            result += prefix_map.get(mask, 0)
            prefix_map[mask] = prefix_map.get(mask, 0) + 1
            for i in range(10):
                toggled: int = mask ^ (1 << i)
                result += prefix_map.get(toggled, 0)
        return result


def test_wonderfulSubstrings_case_1():
    # arrange
    word: str = "aba"
    expected: int = 4

    # act
    actual = Solution().wonderfulSubstrings(word)

    # assert
    assert expected == actual


def test_wonderfulSubstrings_case_2():
    # arrange
    word: str = "aabb"
    expected: int = 9

    # act
    actual = Solution().wonderfulSubstrings(word)

    # assert
    assert expected == actual


def test_wonderfulSubstrings_case_3():
    # arrange
    word: str = "he"
    expected: int = 2

    # act
    actual = Solution().wonderfulSubstrings(word)

    # assert
