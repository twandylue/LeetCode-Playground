struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn make_good(s: String) -> String {
        let mut i: usize = 0;
        let mut result: Vec<char> = Vec::new();
        let s: Vec<char> = s.chars().collect();
        while i < s.len() {
            if result.len() > 0
                && result.last().unwrap().to_lowercase().last().unwrap()
                    == s[i].to_lowercase().last().unwrap()
                && *result.last().unwrap() != s[i]
            {
                result.pop();
            } else {
                result.push(s[i]);
            }
            i += 1;
        }
        result.iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_make_good_case_1() {
        // arrange
        let s: String = "leEeetcode".to_string();
        let expected: String = "leetcode".to_string();

        // act
        let actual = Solution::make_good(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_make_good_case_2() {
        // arrange
        let s: String = "abBAcC".to_string();
        let expected: String = "".to_string();

        // act
        let actual = Solution::make_good(s);

        // assert
        assert_eq!(expected, actual);
    }
}
