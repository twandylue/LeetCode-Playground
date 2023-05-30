class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        result: list[int] = []
        resultLen: float = float("inf")

        have_map: dict[str, int] = {}
        need_map: dict[str, int] = {}
        for c in t:
            need_map[c] = 1 + need_map.get(c, 0)
        need = len(need_map)
        have = 0

        l = 0
        for r in range(len(s)):
            r_c = s[r]
            have_map[r_c] = 1 + have_map.get(r_c, 0)
            if r_c in need_map and have_map[r_c] == need_map[r_c]:
                have += 1

            while have == need:
                if r + 1 - l < resultLen:
                    result = [l, r]
                    resultLen = r + 1 - l

                l_c = s[l]
                have_map[l_c] -= 1
                if l_c in need_map and have_map[l_c] + 1 == need_map[l_c]:
                    have -= 1
                l += 1

        return s[result[0] : result[1] + 1] if resultLen != float("inf") else ""


def test_permutation_in_string_case_1():
    # arrange
    s = "ADOBECODEBANC"
    t = "ABC"
    expected = "BANC"

    # act
    solution = Solution()
    actual = solution.minWindow(s, t)

    # assert
    assert actual == expected


def test_permutation_in_string_case_2():
    # arrange
    s = "a"
    t = "a"
    expected = "a"

    # act
    solution = Solution()
    actual = solution.minWindow(s, t)

    # assert
    assert actual == expected


def test_permutation_in_string_case_3():
    # arrange
    s = "a"
    t = "aa"
    expected = ""

    # act
    solution = Solution()
    actual = solution.minWindow(s, t)

    # assert
    assert actual == expected


def test_permutation_in_string_case_4():
    # arrange
    s = "aab"
    t = "aab"
    expected = "aab"

    # act
    solution = Solution()
    actual = solution.minWindow(s, t)

    # assert
    assert actual == expected
