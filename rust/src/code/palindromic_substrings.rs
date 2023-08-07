struct Solution {}

impl Solution {
    // NOTE: time complexity O(n^2), where n is the length of s
    pub fn count_substrings(s: String) -> i32 {
        let s = s.chars().collect::<Vec<char>>();
        let mut result = 0;

        for i in 0..s.len() {
            // NOTE: for odd substring
            let mut l: usize = i;
            let mut r: usize = i;
            while r < s.len() && s[l] == s[r] {
                result += 1;
                if l.checked_sub(1).is_some() {
                    l -= 1;
                    r += 1;
                } else {
                    break;
                }
            }

            // NOTE: for even substring
            let mut l: usize = i;
            let mut r: usize = i+1;
            while r < s.len() && s[l] == s[r] {
                result += 1;
                if l.checked_sub(1).is_some() {
                    l -= 1;
                    r += 1;
                } else {
                    break;
                }
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn count_substrings_case_1() {
        // arrange
        let s: String = "abc".to_string();
        let expected = 3;

        // act
        let actual = Solution::count_substrings(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn count_substrings_case_2() {
        // arrange
        let s: String = "aaa".to_string();
        let expected = 6;

        // act
        let actual = Solution::count_substrings(s);

        // assert
        assert_eq!(expected, actual);
    }
}
