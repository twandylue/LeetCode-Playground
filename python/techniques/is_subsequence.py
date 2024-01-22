def isSubsequence(self, s: str, p: str, removable: set[int]):
    i: int = 0
    j: int = 0
    while i < len(s):
        if i in removable or (j < len(p) and s[i] != p[j]):
            i += 1
            continue
        if j < len(p) and s[i] == p[j]:
            j += 1
        i += 1

    return j == len(p)
