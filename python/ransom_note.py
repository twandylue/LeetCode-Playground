from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """time complexity: O(n)"""
        ransom_map: dict[str, int] = defaultdict(int)
        magazine_map: dict[str, int] = defaultdict(int)
        for c in magazine:
            magazine_map[c] += 1
        for c in ransomNote:
            ransom_map[c] += 1
            if c not in magazine_map or ransom_map[c] > magazine_map[c]:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        r_count: list[int] = [0] * 26
        m_count: list[int] = [0] * 26
        for c in magazine:
            m_count[ord(c) - ord("a")] += 1
        for c in ransomNote:
            i: int = ord(c) - ord("a")
            r_count[i] += 1
            if m_count[i] == 0 or m_count[i] < r_count[i]:
                return False
        return True


def test_canConstruct_case_1():
    # arrange
    ransomNote: str = "a"
    magazine: str = "b"
    expected: bool = False

    # act
    actual = Solution().canConstruct(ransomNote, magazine)

    # assert
    assert expected == actual


def test_canConstruct_case_2():
    # arrange
    ransomNote: str = "aa"
    magazine: str = "ab"
    expected: bool = False

    # act
    actual = Solution().canConstruct(ransomNote, magazine)

    # assert
    assert expected == actual


def test_canConstruct_case_3():
    # arrange
    ransomNote: str = "aa"
    magazine: str = "aab"
    expected: bool = True

    # act
    actual = Solution().canConstruct(ransomNote, magazine)

    # assert
    assert expected == actual


def test_canConstruct_case_4():
    # arrange
    ransomNote: str = "aa"
    magazine: str = "aab"
    expected: bool = True

    # act
    actual = Solution().canConstruct2(ransomNote, magazine)

    # assert
    assert expected == actual
