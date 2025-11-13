class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """time complexity: O(n)"""
        if len(s1) > len(s2):
            return False
        matches: int = 0
        s1_count: list[int] = [0] * 26
        s2_count: list[int] = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
        for i in range(len(s1_count)):
            if s1_count[i] == s2_count[i]:
                matches += 1
        l: int = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            l_index: int = ord(s2[l]) - ord("a")
            s2_count[l_index] -= 1
            if s2_count[l_index] == s1_count[l_index]:
                matches += 1
            elif s2_count[l_index] + 1 == s1_count[l_index]:
                matches -= 1
            l += 1
            r_index: int = ord(s2[r]) - ord("a")
            s2_count[r_index] += 1
            if s2_count[r_index] == s1_count[r_index]:
                matches += 1
            elif s2_count[r_index] - 1 == s1_count[r_index]:
                matches -= 1
        return matches == 26

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1: list[int] = [0] * 26
        count2: list[int] = [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1
        matches: int = 0
        for i in range(26):
            matches += 1 if count1[i] == count2[i] else 0
        if matches == 26:
            return True
        for i in range(len(s1), len(s2)):
            r_idx: int = ord(s2[i]) - ord("a")
            l_idx: int = ord(s2[i - len(s1)]) - ord("a")
            count2[r_idx] += 1
            count2[l_idx] -= 1
            matches = 0
            for i in range(26):
                matches += 1 if count1[i] == count2[i] else 0
            if matches == 26:
                return True
        return False


def test_permutation_in_string_case1():
    # arrange
    s1 = "ab"
    s2 = "eidbaooo"
    expected = True

    # act
    solution = Solution()
    actual = solution.checkInclusion(s1, s2)

    # assert
    assert actual == expected


def test_permutation_in_string_case2():
    # arrange
    s1 = "ab"
    s2 = "eidboaoo"
    expected = False

    # act
    solution = Solution()
    actual = solution.checkInclusion(s1, s2)

    # assert
    assert actual == expected


def test_permutation_in_string_case3():
    # arrange
    s1 = "ab"
    s2 = "eidboaoo"
    expected = False

    # act
    solution = Solution()
    actual = solution.checkInclusion2(s1, s2)

    # assert
    assert actual == expected


def test_permutation_in_string_case4():
    # arrange
    s1 = "ab"
    s2 = "eidbaooo"
    expected = True

    # act
    solution = Solution()
    actual = solution.checkInclusion2(s1, s2)

    # assert
    assert actual == expected
