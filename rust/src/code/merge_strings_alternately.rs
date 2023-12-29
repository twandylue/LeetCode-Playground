struct Solution {}

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut w1: usize = 0;
        let mut w2: usize = 0;
        let word1: Vec<char> = word1.chars().collect();
        let word2: Vec<char> = word2.chars().collect();
        let mut result: String = "".to_string();

        while w1 < word1.len() && w2 < word2.len() {
            result.push(word1[w1]);
            result.push(word2[w2]);
            w1 += 1;
            w2 += 1;
        }

        while w1 < word1.len() {
            result.push(word1[w1]);
            w1 += 1;
        }

        while w2 < word2.len() {
            result.push(word2[w2]);
            w2 += 1;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_merge_alternately_case_1() {
        // arrange
        let word1: String = "abc".to_string();
        let word2: String = "pqr".to_string();
        let expected: String = "apbqcr".to_string();

        // act
        let actual = Solution::merge_alternately(word1, word2);

        // assert
        assert_eq!(expected, actual);
    }
}
