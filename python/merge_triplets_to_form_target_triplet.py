class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        good: set[int] = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(target):
                if t[i] == v:
                    good.add(i)

        return len(good) == 3


def test_mergeTriplets_case_1():
    # arrange
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    expected = True

    # act
    actual = Solution().mergeTriplets(triplets, target)

    # assert
    assert actual == expected


def test_mergeTriplets_case_2():
    # arrange
    triplets = [[3, 4, 5], [4, 5, 6]]
    target = [3, 2, 5]
    expected = False

    # act
    actual = Solution().mergeTriplets(triplets, target)

    # assert
    assert actual == expected


def test_mergeTriplets_case_3():
    # arrange
    triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
    target = [5, 5, 5]
    expected = True

    # act
    actual = Solution().mergeTriplets(triplets, target)

    # assert
    assert actual == expected
