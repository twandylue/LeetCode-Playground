struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn reverse_words(s: String) -> String {
        let mut s: Vec<char> = s.chars().collect::<Vec<char>>();
        let mut left: usize = 0;
        for right in 0..s.len() {
            if s[right] == ' ' || right == s.len() - 1 {
                let mut tmp_l: usize = left;
                let mut tmp_r: usize = right - 1;
                if right == s.len() - 1 {
                    tmp_r = right;
                }
                while tmp_l < tmp_r {
                    let tmp: char = s[tmp_l];
                    s[tmp_l] = s[tmp_r];
                    s[tmp_r] = tmp;
                    tmp_l += 1;
                    tmp_r -= 1;
                }
                left = right + 1;
            }
        }
        s.iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_words_case_1() {
        // arrange
        let s: String = "Let's take LeetCode contest".to_string();
        let expected: String = "s'teL ekat edoCteeL tsetnoc".to_string();

        // act
        let actual: String = Solution::reverse_words(s);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_reverse_words_case_2() {
        // arrange
        let s: String = "Mr Ding".to_string();
        let expected: String = "rM gniD".to_string();

        // act
        let actual: String = Solution::reverse_words(s);

        // arrange
        assert_eq!(expected, actual);
    }
}
