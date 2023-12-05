struct Solution {}

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();
        let mut i: usize = 0;
        let mut j: usize = 0;
        while i < s.len() && j < t.len() {
            if s[i] == t[j] {
                i += 1;
            }
            j += 1;
        }

        i == s.len()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn is_subsequence_case_1() {
        // arrange
        let s: String = "abc".to_string();
        let t: String = "ahbgdc".to_string();
        let expected: bool = true;

        // act
        let actual = Solution::is_subsequence(s, t);

        // assert
        assert_eq!(expected, actual);
    }
}
