class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        matches = 0
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        s = 0
        for e in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[e]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[s]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            s += 1

        return matches == 26


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
