from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # Time complexity: O(n)
        result: int = 0
        l: int = 0
        count_map: dict[int, int] = defaultdict(int)
        for r in range(len(fruits)):
            count_map[fruits[r]] += 1
            while len(count_map) > 2:
                count_map[fruits[l]] -= 1
                if count_map[fruits[l]] == 0:
                    del count_map[fruits[l]]
                l += 1
            result = max(result, r - l + 1)

        return result


def test_totalFruit_case_1():
    # arrange
    fruits: list[int] = [1, 2, 1]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.totalFruit(fruits)

    # assert
    assert expected == actual


def test_totalFruit_case_2():
    # arrange
    fruits: list[int] = [0, 1, 2, 2]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.totalFruit(fruits)

    # assert
    assert expected == actual


def test_totalFruit_case_3():
    # arrange
    fruits: list[int] = [1, 2, 3, 2, 2]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.totalFruit(fruits)

    # assert
    assert expected == actual
