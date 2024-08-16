class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        """time complexity: O(n)"""
        tokens.sort()
        result: int = 0
        score: int = 0
        l: int = 0
        r: int = len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                result = max(result, score)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return result


def test_bagOfTokensScore_case_1():
    # arrange
    tokens: list[int] = [100]
    power: int = 50
    expected: int = 0

    # act
    solution = Solution()
    actual: int = solution.bagOfTokensScore(tokens, power)

    # assert
    assert expected == actual


def test_bagOfTokensScore_case_2():
    # arrange
    tokens: list[int] = [200, 100]
    power: int = 150
    expected: int = 1

    # act
    solution = Solution()
    actual: int = solution.bagOfTokensScore(tokens, power)

    # assert
    assert expected == actual


def test_bagOfTokensScore_case_3():
    # arrange
    tokens: list[int] = [100, 200, 300, 400]
    power: int = 200
    expected: int = 2

    # act
    solution = Solution()
    actual: int = solution.bagOfTokensScore(tokens, power)

    # assert
    assert expected == actual


def test_bagOfTokensScore_case_4():
    # arrange
    tokens: list[int] = []
    power: int = 85
    expected: int = 0

    # act
    solution = Solution()
    actual: int = solution.bagOfTokensScore(tokens, power)

    # assert
    assert expected == actual


def test_bagOfTokensScore_case_4():
    # arrange
    tokens: list[int] = []
    power: int = 85
    expected: int = 0

    # act
    solution = Solution()
    actual: int = solution.bagOfTokensScore(tokens, power)

    # assert
    assert expected == actual
