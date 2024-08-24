struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn kth_grammar(n: i32, k: i32) -> i32 {
        let mut curr: i32 = 0;
        let mut left: i32 = 0;
        let mut right: i32 = 2_i32.pow(n as u32 - 1);
        for _ in 0..(n - 1) {
            let mid: i32 = (left + right) / 2;
            if k <= mid {
                right = mid;
            } else {
                left = mid + 1;
                curr = if curr == 1 { 0 } else { 1 };
            }
        }
        curr as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_kth_grammar_case_1() {
        // arrange
        let n: i32 = 1;
        let k: i32 = 1;
        let expected: i32 = 0;

        //act
        let actual = Solution::kth_grammar(n, k);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_kth_grammar_case_2() {
        // arrange
        let n: i32 = 2;
        let k: i32 = 1;
        let expected: i32 = 0;

        //act
        let actual = Solution::kth_grammar(n, k);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_kth_grammar_case_3() {
        // arrange
        let n: i32 = 2;
        let k: i32 = 2;
        let expected: i32 = 1;

        //act
        let actual = Solution::kth_grammar(n, k);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_kth_grammar_case_4() {
        // arrange
        let n: i32 = 3;
        let k: i32 = 4;
        let expected: i32 = 0;

        //act
        let actual = Solution::kth_grammar(n, k);

        // assert
        assert_eq!(actual, expected);
    }
}
