struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let colors: Vec<char> = colors.chars().collect();
        let mut l: usize = 0;
        let mut result: i32 = 0;
        for r in 1..colors.len() {
            if colors[l] == colors[r] {
                if needed_time[l] < needed_time[r] {
                    result += needed_time[l];
                    l = r;
                } else {
                    result += needed_time[r];
                }
            } else {
                l = r;
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_min_cost_case_1() {
        // arrange
        let colors: String = "abaac".to_string();
        let needed_time: Vec<i32> = vec![1, 2, 3, 4, 5];
        let expected: i32 = 3;

        // act
        let actual: i32 = Solution::min_cost(colors, needed_time);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_min_cost_case_2() {
        // arrange
        let colors: String = "abc".to_string();
        let needed_time: Vec<i32> = vec![1, 2, 3];
        let expected: i32 = 0;

        // act
        let actual: i32 = Solution::min_cost(colors, needed_time);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_min_cost_case_3() {
        // arrange
        let colors: String = "aabaa".to_string();
        let needed_time: Vec<i32> = vec![1, 2, 3, 4, 1];
        let expected: i32 = 2;

        // act
        let actual: i32 = Solution::min_cost(colors, needed_time);

        // assert
        assert_eq!(expected, actual);
    }
}
