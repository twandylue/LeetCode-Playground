class UnionFind:
    def __init__(self, n: int):
        self._parents: list[int] = [i for i in range(n)]
        self._ranks: list[int] = [1] * n

    def find(self, x: int) -> int:
        while x != self._parents[x]:
            tmp: int = self._parents[x]
            self._parents[x] = self._parents[self._parents[x]]
            x = tmp
        return x

    def union(self, x1: int, x2: int) -> bool:
        p1: int = self.find(x1)
        p2: int = self.find(x2)
        if p1 == p2:
            return False
        if self._ranks[p1] > self._ranks[p2]:
            self._ranks[p1] += self._ranks[p2]
            self._parents[p2] = p1
        else:
            self._ranks[p2] += self._ranks[p2]
            self._parents[p1] = p2
        return True


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """
        NOTE:
        1. Use UnionFind to aggregate accounts with the same email.
        2. time complexity: O(n * m), where n is the number of accounts and m is the number of emails in each account. space complexity: O(n)
        """
        uf: UnionFind = UnionFind(len(accounts))
        # NOTE: email to account idx
        email_to_account: dict[str, int] = {}
        for i in range(len(accounts)):
            for e in accounts[i][1:]:
                if e in email_to_account:
                    uf.union(i, email_to_account[e])
                else:
                    email_to_account[e] = i
        account_with_emails_group: dict[int, list[str]] = {}
        for e, i in email_to_account.items():
            leader: int = uf.find(i)
            if leader in account_with_emails_group:
                account_with_emails_group[leader].append(e)
            else:
                account_with_emails_group[leader] = [e]
        result: list[list[str]] = []
        for i, emails in account_with_emails_group.items():
            result.append([accounts[i][0]] + sorted(emails))
        return result


def test_accountsMerge_case_1():
    # arrange
    accounts: list[list[str]] = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    expected: list[list[str]] = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]

    # act
    solution = Solution()
    actual = solution.accountsMerge(accounts)

    # assert
    assert expected == actual
