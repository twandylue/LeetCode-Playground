class Solution:
    def defangIPaddr(self, address: str) -> str:
        result: str = ""
        for c in address:
            if c == ".":
                result += "[.]"
                continue
            result += c
        return result


def test_defangIPaddr_1():
    """This is a test case"""
    # arrange
    address: str = "1.1.1.1"
    expected: str = "1[.]1[.]1[.]1"

    # act
    actual = Solution().defangIPaddr(address)

    # assert
    assert expected == actual


def test_defangIPaddr_2():
    """This is a test case"""
    # arrange
    address: str = "255.100.50.0"
    expected: str = "255[.]100[.]50[.]0"

    # act
    actual = Solution().defangIPaddr(address)

    # assert
    assert expected == actual
