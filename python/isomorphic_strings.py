class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """time complexity: O(n), space complexity: O(n)"""
        if len(s) != len(t):
            return False
        s_t_map: dict[str, str] = {}
        t_s_map: dict[str, str] = {}
        for i in range(len(s)):
            if s[i] not in s_t_map:
                s_t_map[s[i]] = t[i]
            elif s_t_map[s[i]] != t[i]:
                return False
            if t[i] not in t_s_map:
                t_s_map[t[i]] = s[i]
            elif t_s_map[t[i]] != s[i]:
                return False
        return True


def test_isIsomorphic_case_1():
    # arrange
    s: str = "egg"
    t: str = "add"
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isIsomorphic(s, t)

    # assert
    assert expected == actual


def test_isIsomorphic_case_2():
    # arrange
    s: str = "foo"
    t: str = "bar"
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isIsomorphic(s, t)

    # assert
    assert expected == actual


def test_isIsomorphic_case_3():
    # arrange
    s: str = "paper"
    t: str = "title"
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isIsomorphic(s, t)

    # assert
    assert expected == actual


def test_isIsomorphic_case_4():
    # arrange
    s: str = "badc"
    t: str = "baba"
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isIsomorphic(s, t)

    # assert
    assert expected == actual
