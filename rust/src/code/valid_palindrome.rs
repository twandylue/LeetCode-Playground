pub struct Solution {}

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let iter = s
            .chars()
            .filter(|c| c.is_alphanumeric())
            .map(|x| x.to_ascii_lowercase());

        return iter.clone().eq(iter.rev());
    }

    pub fn is_palindrome2(s: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let mut l: usize = 0;
        let mut r: usize = s.len() - 1;
        while l < r {
            if !s[l].is_alphanumeric() {
                l += 1;
                continue;
            }
            if !s[r].is_alphanumeric() {
                if r.checked_sub(1).is_none() {
                    return false;
                }
                r -= 1;
                continue;
            }
            if s[l].to_ascii_lowercase() != s[r].to_ascii_lowercase() {
                return false;
            }

            l += 1;

            if r.checked_sub(1).is_none() {
                break;
            }
            r -= 1;
        }

        true
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn is_palindrome_case_1() {
        let s = "A man, a plan, a canal: Panama".to_string();
        let expected = true;
        let actual = Solution::is_palindrome(s);
        assert_eq!(actual, expected);
    }

    #[test]
    fn is_palindrome_case_2() {
        let s2 = "race a car".to_string();
        let expected2 = false;
        let actual2 = Solution::is_palindrome(s2);
        assert_eq!(actual2, expected2);
    }

    #[test]
    fn is_palindrome_case_3() {
        let s3 = " ".to_string();
        let expected3 = true;
        let actual3 = Solution::is_palindrome(s3);
        assert_eq!(actual3, expected3);
    }

    #[test]
    fn is_palindrome_case_4() {
        let s = "A man, a plan, a canal: Panama".to_string();
        let expected = true;
        let actual = Solution::is_palindrome2(s);
        assert_eq!(actual, expected);
    }

    #[test]
    fn is_palindrome_case_5() {
        let s2 = "race a car".to_string();
        let expected2 = false;
        let actual2 = Solution::is_palindrome2(s2);
        assert_eq!(actual2, expected2);
    }

    #[test]
    fn is_palindrome_case_6() {
        let s3 = " ".to_string();
        let expected3 = true;
        let actual3 = Solution::is_palindrome2(s3);
        assert_eq!(actual3, expected3);
    }
}
