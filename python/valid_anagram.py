class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alph = [0] * 26
        for i in range(0, len(s)):
            alph[ord(s[i]) - ord("a")] += 1
            alph[ord(t[i]) - ord("a")] -= 1

        for i in range(0, len(alph)):
            if alph[i] != 0:
                return False

        return True


def test_isAnagram_case_1():
    # arrange
    s: str = "anagram"
    t: str = "nagaram"
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isAnagram(s, t)

    # assert
    assert expected == actual


def test_isAnagram_case_2():
    # arrange
    s: str = "aacc"
    t: str = "ccac"
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isAnagram(s, t)

    # assert
    assert expected == actual
