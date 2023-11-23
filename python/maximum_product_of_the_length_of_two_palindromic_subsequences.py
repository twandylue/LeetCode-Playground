class Solution:
    def maxProduct(self, s: str) -> int:
        n: int = len(s)
        pali: dict[str, int] = dict()
        for mask in range(1, 1 << n):
            subseq: str = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)

        result: int = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2:
                    continue
                else:
                    result = max(result, pali[m1] * pali[m2])

        return result


def test_maxProduct_case_1():
    # arrange
    s: str = "leetcodecom"
    expected: int = 9

    # act
    solution = Solution()
    actual = solution.maxProduct(s)

    # assert
    assert expected == actual


def test_maxProduct_case_2():
    # arrange
    s: str = "bb"
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.maxProduct(s)

    # assert
    assert expected == actual


def test_maxProduct_case_3():
    # arrange
    s: str = "accbcaxxcxx"
    expected: int = 25

    # act
    solution = Solution()
    actual = solution.maxProduct(s)

    # assert
    assert expected == actual
