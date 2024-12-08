class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: list[str]) -> str:
        """time complexity: O(n) where n is the number of string in strs, space complexity: O(n)"""
        # write your code here
        result: str = ""
        for i in range(len(strs)):
            result += str(len(strs[i])) + "#" + strs[i]

        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s: str) -> list[str]:
        """time complexity: O(n), space complexity: O(n)"""
        # write your code here
        result: list[str] = list()
        l: int = 0
        r: int = 0
        while r < len(s):
            while r < len(s) and s[r] != "#":
                r += 1

            length: int = int(s[l:r])
            result.append(s[r + 1 : r + 1 + length])
            r = r + 1 + length
            l = r

        return result


def test_encode_decode_strings_case_1():
    # arrange
    input: list[str] = ["lint", "code", "love", "you"]
    expected: list[str] = ["lint", "code", "love", "you"]

    # act
    solution = Solution()
    encode_result = solution.encode(input)
    decode_result = solution.decode(encode_result)

    # assert
    assert expected == decode_result


def test_encode_decode_strings_case_2():
    # arrange
    input: list[str] = ["we", "say", ":", "yes"]
    expected: list[str] = ["we", "say", ":", "yes"]

    # act
    solution = Solution()
    encode_result = solution.encode(input)
    decode_result = solution.decode(encode_result)

    # assert
    assert expected == decode_result


def test_encode_decode_strings_case_3():
    # arrange
    input: list[str] = ["C#", "&", "~Xp|F", "R4QBf9g=_"]
    expected: list[str] = ["C#", "&", "~Xp|F", "R4QBf9g=_"]

    # act
    solution = Solution()
    encode_result = solution.encode(input)
    decode_result = solution.decode(encode_result)

    # assert
    assert expected == decode_result
