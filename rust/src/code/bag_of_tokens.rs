struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn bag_of_tokens_score(mut tokens: Vec<i32>, mut power: i32) -> i32 {
        use std::cmp::max;
        if tokens.len() == 0 {
            return 0;
        }
        tokens.sort();
        let mut result: i32 = 0;
        let mut score: i32 = 0;
        let mut l: usize = 0;
        let mut r: usize = tokens.len() - 1;
        while l <= r {
            if power >= tokens[l] {
                power -= tokens[l];
                score += 1;
                l += 1;
                result = max(result, score);
            } else if score > 0 {
                power += tokens[r];
                score -= 1;
                r -= 1;
            } else {
                break;
            }
            dd
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_bag_of_tokens_score_case_1() {
        // arrange
        let tokens: Vec<i32> = vec![100];
        let power: i32 = 50;
        let expected: i32 = 0;

        // act
        let actual: i32 = Solution::bag_of_tokens_score(tokens, power);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_bag_of_tokens_score_case_2() {
        // arrange
        let tokens: Vec<i32> = vec![200, 100];
        let power: i32 = 150;
        let expected: i32 = 1;

        // act
        let actual: i32 = Solution::bag_of_tokens_score(tokens, power);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_bag_of_tokens_score_case_3() {
        // arrange
        let tokens: Vec<i32> = vec![100, 200, 300, 400];
        let power: i32 = 200;
        let expected: i32 = 2;

        // act
        let actual: i32 = Solution::bag_of_tokens_score(tokens, power);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_bag_of_tokens_score_case_4() {
        // arrange
        let tokens: Vec<i32> = vec![];
        let power: i32 = 85;
        let expected: i32 = 0;

        // act
        let actual: i32 = Solution::bag_of_tokens_score(tokens, power);

        // arrange
        assert_eq!(expected, actual);
    }
}
