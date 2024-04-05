struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn remove_stars(s: String) -> String {
        let mut stack: Vec<char> = Vec::new();
        let s: Vec<char> = s.chars().collect();
        for i in 0..s.len() {
            if s[i] == '*' {
                stack.pop().unwrap();
            } else {
                stack.push(s[i]);
            }
        }

        stack.iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_remove_stars_case_1() {
        // arrange
        let s: String = "leet**cod*e".to_string();
        let expected: String = "lecoe".to_string();

        // act
        let actual = Solution::remove_stars(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_remove_stars_case_2() {
        // arrange
        let s: String = "erase*****".to_string();
        let expected: String = "".to_string();

        // act
        let actual = Solution::remove_stars(s);

        // assert
        assert_eq!(expected, actual);
    }
}
