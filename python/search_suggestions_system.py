class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        result: list[int] = list()
        products.sort()
        l: int = 0
        r: int = len(products) - 1
        i: int = 0
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            currLen: int = r - l + 1
            if currLen >= 3:
                result.append(products[l : l + 3])
            else:
                result.append(products[l : r + 1])

        return result


def test_suggestedProducts_case_1():
    # arrange
    products: list[str] = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord: str = "mouse"
    expected: list[str] = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]

    # act
    solution = Solution()
    actual = solution.suggestedProducts(products, searchWord)

    # assert
    assert expected == actual


def test_suggestedProducts_case_2():
    # arrange
    products: list[str] = ["havana"]
    searchWord: str = "havana"
    expected: list[str] = [
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
    ]

    # act
    solution = Solution()
    actual = solution.suggestedProducts(products, searchWord)

    # assert
    assert expected == actual


def test_suggestedProducts_case_3():
    # arrange
    products: list[str] = ["bags", "baggage", "banner", "box", "cloths"]
    searchWord: str = "bags"
    expected: list[str] = [
        ["baggage", "bags", "banner"],
        ["baggage", "bags", "banner"],
        ["baggage", "bags"],
        ["bags"],
    ]

    # act
    solution = Solution()
    actual = solution.suggestedProducts(products, searchWord)

    # assert
    assert expected == actual


def test_suggestedProducts_case_4():
    # arrange
    products: list[str] = ["havana"]
    searchWord: str = "tatiana"
    expected: list[str] = [[], [], [], [], [], [], []]

    # act
    solution = Solution()
    actual = solution.suggestedProducts(products, searchWord)

    # assert
    assert expected == actual
