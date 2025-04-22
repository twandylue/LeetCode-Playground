class UnionFind:
    def __init__(self, n: int):
        self._indep: int = n
        self._parent: list[int] = [i for i in range(n)]
        self._rank: list[int] = [1] * n

    def find(self, n: int) -> int:
        while n != self._parent[n]:
            n = self._parent[n]
        return n

    def union(self, u: int, v: int) -> bool:
        pu: int = self.find(u)
        pv: int = self.find(v)
        if pu == pv:
            return False
        if self._rank[pv] > self._rank[pu]:
            pu, pv = pv, pu
        self._parent[pv] = pu
        self._indep -= 1
        return True


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """
        NOTE:
        1. Use UnionFind to aggregate accounts with the same email.
        2. time complexity: O(n * m), where n is the number of accounts and m is the number of emails in each account. space complexity: O(n)
        """
        uf: UnionFind = UnionFind(len(accounts))
        email_accounts_map: dict[str, int] = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in email_accounts_map:
                    uf.union(email_accounts_map[email], i)
                else:
                    email_accounts_map[email] = i
        account_emails_map: dict[int, list[str]] = {}
        for email, account_id in email_accounts_map.items():
            parent_id: int = uf.find(account_id)
            if parent_id in account_emails_map:
                account_emails_map[parent_id].append(email)
            else:
                account_emails_map[parent_id] = [email]
        result: list[list[str]] = []
        for id, emails in account_emails_map.items():
            result.append([accounts[id][0]] + sorted(emails))
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
