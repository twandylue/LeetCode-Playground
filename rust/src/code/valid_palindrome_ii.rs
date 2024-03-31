struct Solution {}

impl Solution {
    // NOTE: time complexity O(n)
    pub fn valid_palindrome(s: String) -> bool {
        if s.len() < 1 {
            return true;
        }
        let s: Vec<char> = s.chars().collect();
        let mut l: usize = 0;
        let mut r: usize = s.len() - 1;
        while l < r {
            if s[l] != s[r] {
                return Self::is_palindrome(&s[l + 1..r + 1]) || Self::is_palindrome(&s[l..r]);
            }
            l += 1;
            r -= 1;
        }
        true
    }

    fn is_palindrome(s: &[char]) -> bool {
        if s.len() < 1 {
            return true;
        }
        let mut l: usize = 0;
        let mut r: usize = s.len() - 1;
        while l < r {
            if s[l] != s[r] {
                return false;
            }
            l += 1;
            r -= 1;
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_palindrome_case_1() {
        // arrange
        let s: String = "aba".to_string();
        let expected: bool = true;

        // act
        let actual = Solution::valid_palindrome(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_valid_palindrome_case_2() {
        // arrange
        let s: String = "abca".to_string();
        let expected: bool = true;

        // act
        let actual = Solution::valid_palindrome(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_valid_palindrome_case_3() {
        // arrange
        let s: String = "acbca".to_string();
        let expected: bool = true;

        // act
        let actual = Solution::valid_palindrome(s);

        // assert
        assert_eq!(expected, actual);
    }
}
