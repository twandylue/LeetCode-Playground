struct Solution {}

impl Solution {
    // NOTE: time limit O(logN)
    pub fn my_pow(x: f64, n: i32) -> f64 {
        let result = Self::helper(x, n);
        // let result = Self::helper(x, n.abs());

        return if n >= 0 { result } else { 1_f64 / result };
    }

    fn helper(x: f64, n: i32) -> f64 {
        if x == 0_f64 {
            return 0_f64;
        }

        if n == 0 {
            return 1_f64;
        }

        let mut result = Self::helper(x, n / 2);
        result *= result;

        return if n % 2 == 0 { result } else { x * result };
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_my_pow_case_1() {
        // arrange
        let x = 2.0;
        let n = 10;
        let expected = 1024.0;

        // act
        let actual = Solution::my_pow(x, n);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    // TODO:
    #[ignore]
    fn test_my_pow_case_2() {
        // arrange
        let x = 2.1;
        let n = 3;
        let expected = 9.261;

        // act
        let actual = Solution::my_pow(x, n);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_my_pow_case_3() {
        // arrange
        let x = 2.0;
        let n = -2;
        let expected = 0.25;

        // act
        let actual = Solution::my_pow(x, n);

        // assert
        assert_eq!(actual, expected);
    }
}
