class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        matches: int = 0
        result: list[int] = []
        s_count: list[int] = [0] * 26
        p_count: list[int] = [0] * 26

        for i in range(len(p)):
            s_count[ord(s[i]) - ord("a")] += 1
            p_count[ord(p[i]) - ord("a")] += 1

        for i in range(26):
            matches += 1 if s_count[i] == p_count[i] else 0

        l: int = 0
        for r in range(len(p), len(s)):
            if matches == 26:
                result.append(l)

            rightIndex: int = ord(s[r]) - ord("a")
            s_count[rightIndex] += 1
            if s_count[rightIndex] == p_count[rightIndex]:
                matches += 1
            elif s_count[rightIndex] - 1 == p_count[rightIndex]:
                matches -= 1

            leftIndex: int = ord(s[l]) - ord("a")
            s_count[leftIndex] -= 1
            if s_count[leftIndex] == p_count[leftIndex]:
                matches += 1
            elif s_count[leftIndex] + 1 == p_count[leftIndex]:
                matches -= 1

            l += 1

        result.append(l) if matches == 26 else None

        return result


def test_find_all_anagrams_in_a_string_case_1():
    # arrange
    s = "cbaebabacd"
    p = "abc"
    expected = [0, 6]

    # act
    solution = Solution()
    actual = solution.findAnagrams(s, p)

    # assert
    assert actual == expected


def test_find_all_anagrams_in_a_string_case_2():
    # arrange
    s = "abab"
    p = "ab"
    expected = [0, 1, 2]

    # act
    solution = Solution()
    actual = solution.findAnagrams(s, p)

    # assert
    assert actual == expected
