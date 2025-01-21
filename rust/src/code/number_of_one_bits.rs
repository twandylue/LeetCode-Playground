struct Solution;

impl Solution {
    // time complexity: O(1)
    pub fn hamming_weight(n: i32) -> i32 {
        let mut result: i32 = 0;
        for i in 0..32 {
            if n & (1 << i) != 0 {
                result += 1;
            }
        }
        result
    }
}

#[cfg(test)]
pub mod test {
    use super::Solution;

    #[test]
    fn test_hamming_weight_case_1() {
        // arrange
        let n: i32 = 11;
        let expected: i32 = 3;

        // act
        let actual = Solution::hamming_weight(n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_hamming_weight_case_2() {
        // arrange
        let n: i32 = 128;
        let expected: i32 = 1;

        // act
        let actual = Solution::hamming_weight(n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_hamming_weight_case_3() {
        // arrange
        let n: i32 = 2147483645;
        let expected: i32 = 30;

        // act
        let actual = Solution::hamming_weight(n);

        // assert
        assert_eq!(expected, actual);
    }
}
