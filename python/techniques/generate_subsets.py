def subsets(self, nums: list[int]) -> list[list[int]]:
    n: int = len(nums)
    result: list[list[int]] = [[]]

    for mask in range(1, 1 << n):
        subSet: list[int] = list()
        for i in range(n):
            if mask & (1 << i):
                subSet.append(nums[i])
        result.append(subSet)

    return result
