class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        result: int = 0
        l: int = 0
        r: int = len(people) - 1
        while l <= r:
            remain: int = limit - people[r]
            r -= 1
            if l <= r and remain >= people[l]:
                l += 1
            result += 1

        return result


def test_numRescueBoats_case_1():
    # arrange
    people: list[int] = [1, 2]
    limit: int = 3
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.numRescueBoats(people, limit)

    # assert
    assert expected == actual


def test_numRescueBoats_case_2():
    # arrange
    people: list[int] = [3, 5, 3, 4]
    limit: int = 5
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.numRescueBoats(people, limit)

    # assert
    assert expected == actual
