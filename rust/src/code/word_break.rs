struct Solution {}

impl Solution {
    // NOTE: time complexity O(n * m), space complexity O(n), where n is the length of s and m is
    // the length of word_dict
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let mut dp: Vec<bool> = vec![false; s.len() + 1];
        dp[s.len()] = true;
        let s = s.chars().collect::<Vec<char>>();

        for i in (0..s.len()).rev() {
            for w in word_dict.iter() {
                if i + w.len() <= s.len() && s[i..(i + w.len())].iter().collect::<String>() == *w {
                    dp[i] = dp[i + w.len()];
                }
                if dp[i] {
                    break;
                }
            }
        }

        dp[0]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_word_break_case_1() {
        // arrange
        let s = "leetcode".to_string();
        let word_dict = vec!["leet".to_string(), "code".to_string()];
        let expected = true;

        // act
        let result = Solution::word_break(s, word_dict);

        // assert
        assert_eq!(result, expected);
    }

    #[test]
    fn test_word_break_case_2() {
        // arrange
        let s = "applepenapple".to_string();
        let word_dict = vec!["apple".to_string(), "pen".to_string(), "apple".to_string()];
        let expected = true;

        // act
        let result = Solution::word_break(s, word_dict);

        // assert
        assert_eq!(result, expected);
    }

    #[test]
    fn test_word_break_case_3() {
        // arrange
        let s = "catsandog".to_string();
        let word_dict = vec![
            "cats".to_string(),
            "dog".to_string(),
            "sand".to_string(),
            "and".to_string(),
            "cat".to_string(),
        ];
        let expected = false;

        // act
        let result = Solution::word_break(s, word_dict);

        // assert
        assert_eq!(result, expected);
    }

    #[test]
    fn test_word_break_case_4() {
        // arrange
        let s = "abcd".to_string();
        let word_dict = vec![
            "a".to_string(),
            "abc".to_string(),
            "b".to_string(),
            "cd".to_string(),
        ];
        let expected = true;

        // act
        let result = Solution::word_break(s, word_dict);

        // assert
        assert_eq!(result, expected);
    }
}
