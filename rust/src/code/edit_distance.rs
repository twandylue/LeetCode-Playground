use std::cmp::min;

pub struct Solution {}

impl Solution {
    fn helper(word1: String, word2: String, cache: &mut Vec<Vec<i32>>) -> i32 {
        let n1 = word1.len();
        let n2 = word2.len();

        if cache[n1][n2] != 0 {
            return cache[n1][n2];
        }

        if n1 == 0 {
            cache[n1][n2] = n2 as i32;
            return cache[n1][n2];
        }

        if n2 == 0 {
            cache[n1][n2] = n1 as i32;
            return cache[n1][n2];
        }

        if word1.chars().last() == word2.chars().last() {
            cache[n1][n2] = Self::helper(
                word1.as_str()[..word1.len() - 1].to_string(),
                word2.as_str()[..word2.len() - 1].to_string(),
                cache,
            );
            return cache[n1][n2];
        }

        cache[n1][n2] = 1 + min(
            min(
                Self::helper(
                    word1.clone(),
                    word2.as_str()[..word2.len() - 1].to_string(),
                    cache,
                ),
                Self::helper(
                    word1.clone().as_str()[..word1.len() - 1].to_string(),
                    word2.clone(),
                    cache,
                ),
            ),
            Self::helper(
                word1.as_str()[..word1.len() - 1].to_string(),
                word2.as_str()[..word2.len() - 1].to_string(),
                cache,
            ),
        );

        return cache[n1][n2];
    }

    pub fn min_distance(word1: String, word2: String) -> i32 {
        let mut cache = vec![vec![0; word2.len() + 1]; word1.len() + 1];

        return Self::helper(word1, word2, &mut cache);
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        // arrange
        let word1 = "horse".to_string();
        let word2 = "ros".to_string();
        let expected = 3;

        // act
        let actual = Solution::min_distance(word1, word2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        // arrange
        let word1 = "intention".to_string();
        let word2 = "execution".to_string();
        let expected = 5;

        // act
        let actual = Solution::min_distance(word1, word2);

        // assert
        assert_eq!(expected, actual);
    }
}
