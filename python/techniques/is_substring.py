# NOTE: O(m+n)
# ref: find_the_index_of_the_first_occurrence_in_a_string.py
def is_substring(haystack: str, needle: str) -> bool:
    """Find out if needle is a substring of haystack"""
    result: bool = False
    if len(needle) == 0:
        return 0

    lps: list[int] = [0] * len(needle)
    i: int = 1
    pre_lps: int = 0
    while i < len(needle):
        if needle[pre_lps] == needle[i]:
            pre_lps += 1
            lps[i] = pre_lps
            i += 1
        elif pre_lps == 0:
            lps[i] = 0
            i += 1
        else:
            pre_lps = lps[pre_lps - 1]

    m: int = 0
    n: int = 0
    while m < len(haystack):
        if haystack[m] == needle[n]:
            m += 1
            n += 1
        else:
            if n == 0:
                m += 1
            else:
                n = lps[n - 1]

        if n == len(needle):
            result = True
            # return m - n # For first occurence position

    # return -1
    return result
