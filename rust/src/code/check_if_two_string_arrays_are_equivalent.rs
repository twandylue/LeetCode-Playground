struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        let mut new_word1: Vec<Vec<char>> = Vec::new();
        let mut new_word2: Vec<Vec<char>> = Vec::new();
        for word in word1 {
            new_word1.push(word.chars().collect::<Vec<char>>());
        }
        for word in word2 {
            new_word2.push(word.chars().collect::<Vec<char>>());
        }
        let mut w1: usize = 0;
        let mut w2: usize = 0;
        let mut i: usize = 0;
        let mut j: usize = 0;
        while w1 < new_word1.len() && w2 < new_word2.len() {
            if new_word1[w1][i] != new_word2[w2][j] {
                return false;
            }
            i += 1;
            j += 1;
            if i == new_word1[w1].len() {
                w1 += 1;
                i = 0;
            }
            if j == new_word2[w2].len() {
                w2 += 1;
                j = 0;
            }
        }
        if w1 != new_word1.len() || w2 != new_word2.len() {
            return false;
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_array_strings_are_equal_case_1() {
        // arrange
        let word1: Vec<String> = vec!["ab".to_string(), "c".to_string()];
        let word2: Vec<String> = vec!["a".to_string(), "bc".to_string()];
        let expected: bool = true;

        // act
        let actual = Solution::array_strings_are_equal(word1, word2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_array_strings_are_equal_case_2() {
        // arrange
        let word1: Vec<String> = vec!["a".to_string(), "cb".to_string()];
        let word2: Vec<String> = vec!["ab".to_string(), "c".to_string()];
        let expected: bool = false;

        // act
        let actual = Solution::array_strings_are_equal(word1, word2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_array_strings_are_equal_case_3() {
        // arrange
        let word1: Vec<String> = vec!["abc".to_string(), "d".to_string(), "defg".to_string()];
        let word2: Vec<String> = vec!["abcddefg".to_string()];
        let expected: bool = true;

        // act
        let actual = Solution::array_strings_are_equal(word1, word2);

        // assert
        assert_eq!(actual, expected);
    }
}
