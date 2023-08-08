struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n^2)
    pub fn longest_palindrome(s: String) -> String {
        let s: &[char] = &s.chars().collect::<Vec<char>>();
        let mut result: String = String::new();
        let mut result_len: usize = 0;

        for i in 0..s.len() {
            // NOTE: for odd length
            let mut l: usize = i;
            let mut r: usize = i;
            while r < s.len() && s[l] == s[r] {
                if r - l + 1 > result_len {
                    result_len = r - l + 1;
                    result = s[l..r + 1].to_vec().iter().collect::<String>();
                }

                if l > 0 {
                    l -= 1;
                    r += 1;
                } else {
                    break;
                }
            }

            // NOTE: for even length
            l = i;
            r = i + 1;
            while r < s.len() && s[l] == s[r] {
                if r - l + 1 > result_len {
                    result_len = r - l + 1;
                    result = s[l..r + 1].to_vec().iter().collect::<String>();
                }

                if l > 0 {
                    l -= 1;
                    r += 1;
                } else {
                    break;
                }
            }
        }

        return result;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn longest_palindrome_case_1() {
        // arrange
        let s: String = "babad".to_string();
        let expected = "bab".to_string();

        // act
        let actual = Solution::longest_palindrome(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn longest_palindrome_case_2() {
        // arrange
        let s: String = "cbbd".to_string();
        let expected = "bb".to_string();

        // act
        let actual = Solution::longest_palindrome(s);

        // assert
        assert_eq!(expected, actual);
    }
}
