class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        emailSet: set[tuple[str, str]] = set()
        for email in emails:
            x: list[str] = email.split("@")
            localName: str = x[0]
            domainName: str = x[1]
            localName = localName.replace(".", "")
            i: int = localName.find("+")
            if i != -1:
                localName = localName[:i]

            emailSet.add((localName, domainName))

        return len(emailSet)


def test_numUniqueEmails_case_1():
    # arrange
    emails: list[str] = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.numUniqueEmails(emails)

    # assert
    assert expected == actual


def test_numUniqueEmails_case_2():
    # arrange
    emails: list[str] = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.numUniqueEmails(emails)

    # assert
    assert expected == actual
