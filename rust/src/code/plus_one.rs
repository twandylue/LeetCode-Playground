struct Solution {}

impl Solution {
    // NOTE: time complexity O(n), space complexity O(n)
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut digits: Vec<i32> = digits.into_iter().rev().collect::<Vec<i32>>();
        let mut carry: i32 = 0;

        digits[0] += 1;
        if digits[0] / 10 > 0 {
            carry = digits[0] / 10;
            digits[0] = digits[0] % 10;
        }

        for i in 1..digits.len() {
            digits[i] += carry;
            carry = digits[i] / 10;
            if carry > 0 {
                digits[i] = digits[i] % 10;
            }
        }

        if carry > 0 {
            digits.push(1);
        }

        digits.into_iter().rev().collect::<Vec<i32>>()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_plus_one_case_1() {
        // arrange
        let digits = vec![1, 2, 3];
        let expected = vec![1, 2, 4];

        // act
        let actual = Solution::plus_one(digits);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_plus_one_case_2() {
        // arrange
        let digits = vec![4, 3, 2, 1];
        let expected = vec![4, 3, 2, 2];

        // act
        let actual = Solution::plus_one(digits);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_plus_one_case_3() {
        // arrange
        let digits = vec![0];
        let expected = vec![1];

        // act
        let actual = Solution::plus_one(digits);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_plus_one_case_4() {
        // arrange
        let digits = vec![9, 9, 9, 9];
        let expected = vec![1, 0, 0, 0, 0];

        // act
        let actual = Solution::plus_one(digits);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_plus_one_case_5() {
        // arrange
        let digits = vec![9, 9, 9, 8];
        let expected = vec![9, 9, 9, 9];

        // act
        let actual = Solution::plus_one(digits);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_plus_one_case_6() {
        // arrange
        let digits = vec![9];
        let expected = vec![1, 0];

        // act
        let actual = Solution::plus_one(digits);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_plus_one_case_7() {
        // arrange
        let digits = vec![8, 9, 9, 9];
        let expected = vec![9, 0, 0, 0];

        // act
        let actual = Solution::plus_one(digits);

        // assert
        assert_eq!(actual, expected);
    }
}
