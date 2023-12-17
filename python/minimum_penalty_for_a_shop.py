class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ps1: list[int] = [0] * (len(customers) + 1)
        ps2: list[int] = [0] * (len(customers) + 1)

        curr: int = 0
        for i in range(0, len(customers)):
            if customers[i] == "N":
                curr += 1
            ps1[i + 1] = curr

        curr = 0
        for i in reversed(range(0, len(customers))):
            if customers[i] == "Y":
                curr += 1
            ps2[i] = curr

        minP: int = float("inf")
        minIndex: int = 0
        for i in range(len(ps1)):
            if ps1[i] + ps2[i] < minP:
                minP = ps1[i] + ps2[i]
                minIndex = i

        return minIndex


def test_bestClosingTime_case_1():
    # arrange
    customers: str = "YYNY"
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.bestClosingTime(customers)

    # assert
    assert expected == actual


def test_bestClosingTime_case_2():
    # arrange
    customers: str = "NNNNN"
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.bestClosingTime(customers)

    # assert
    assert expected == actual


def test_bestClosingTime_case_3():
    # arrange
    customers: str = "YYYY"
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.bestClosingTime(customers)

    # assert
    assert expected == actual
