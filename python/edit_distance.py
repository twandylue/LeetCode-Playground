# The Levenshtein Algorithm
# ref:
# 1. https://medium.com/cuelogic-technologies/the-levenshtein-algorithm-916db91843ba
# 2. https://www.youtube.com/watch?v=tG4IeY01-xw&t=5610s&ab_channel=TsodingDaily
#
# - [x] Recursive
# - [x] Cache
# - [x] 2D map cache
# - [ ] Backward


class Solution:
    def minDistance_rec(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if word1[-1] == word2[-1]:
            return self.minDistance_rec(word1[:-1], word2[:-1])  # ignore

        return 1 + min(
            self.minDistance_rec(word1, word2[:-1]),  # add
            self.minDistance_rec(word1[:-1], word2),  # remove
            self.minDistance_rec(word1[:-1], word2[:-1]),  # ignore
        )

    def minDistance_rec_cache(self, word1: str, word2: str) -> int:
        cache = []
        for _ in range(len(word1) + 1):
            cache.append([None] * (len(word2) + 1))

        return self.helper_rec_cache(word1, word2, cache)

    def helper_rec_cache(self, word1: str, word2: str, cache) -> int:
        s1 = len(word1)
        s2 = len(word2)

        if cache[s1][s2] is not None:
            return cache[s1][s2]

        if s1 == 0:
            cache[s1][s2] = s2
            return cache[s1][s2]
        if s2 == 0:
            cache[s1][s2] = s1
            return cache[s1][s2]
        if word1[s1 - 1] == word2[s2 - 1]:
            cache[s1][s2] = self.helper_rec_cache(word1[:-1], word2[:-1], cache)
            return cache[s1][s2]

        cache[s1][s2] = 1 + min(
            self.helper_rec_cache(word1[:-1], word2[:-1], cache),
            self.helper_rec_cache(word1, word2[:-1], cache),
            self.helper_rec_cache(word1[:-1], word2, cache),
        )

        return cache[s1][s2]

    def minDistance_2D_cache(self, word1: str, word2: str) -> int:
        cache = []
        for _ in range(len(word1) + 1):
            cache.append([0] * (len(word2) + 1))

        return self.helper_2D_cache(word1, word2, cache)

    def helper_2D_cache(self, word1: str, word2: str, cache) -> int:
        for n2 in range(1, len(word2) + 1):
            n1 = 0
            cache[n1][n2] = n2
        for n1 in range(1, len(word1) + 1):
            n2 = 0
            cache[n1][n2] = n1

        for n1 in range(1, len(word1) + 1):
            for n2 in range(1, len(word2) + 1):
                if word1[n1 - 1] == word2[n2 - 1]:
                    cache[n1][n2] = cache[n1 - 1][n2 - 1]
                    continue
                cache[n1][n2] = 1 + min(
                    cache[n1 - 1][n2], cache[n1][n2 - 1], cache[n1 - 1][n2 - 1]
                )

        return cache[len(word1)][len(word2)]


def test_rec_case1():
    solution = Solution()
    actual_rec = solution.minDistance_rec("horse", "ros")
    assert actual_rec == 3


def test_rec_case2():
    solution = Solution()
    actual_rec = solution.minDistance_rec("intention", "execution")
    assert actual_rec == 5


def test_rec_cache_case1():
    solution = Solution()
    actual_rec = solution.minDistance_rec_cache("horse", "ros")
    assert actual_rec == 3


def test_rec_cache_case2():
    solution = Solution()
    actual_rec = solution.minDistance_rec_cache("intention", "execution")
    assert actual_rec == 5


def test_map_cache_case1():
    solution = Solution()
    actual_rec = solution.minDistance_2D_cache("horse", "ros")
    assert actual_rec == 3


def test_map_cache_case2():
    solution = Solution()
    actual_rec = solution.minDistance_2D_cache("intention", "execution")
    assert actual_rec == 5
