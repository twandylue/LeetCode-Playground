struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut negative: i32 = 0;
        for num in nums.iter() {
            if num < &0 {
                negative += 1
            } else if num == &0 {
                return 0;
            }
        }

        return if negative % 2 == 0 { 1 } else { -1 };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn two_array_sign_case_1() {
        // arrange
        let numbers: Vec<i32> = vec![-1, -2, -3, -4, 3, 2, 1];
        let expected: i32 = 1;

        // act
        let actual = Solution::array_sign(numbers);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn two_array_sign_case_2() {
        // arrange
        let numbers: Vec<i32> = vec![
            41, 65, 14, 80, 20, 10, 55, 58, 24, 56, 28, 86, 96, 10, 3, 84, 4, 41, 13, 32, 42, 43,
            83, 78, 82, 70, 15, -41,
        ];
        let expected: i32 = -1;

        // act
        let actual = Solution::array_sign(numbers);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn two_array_sign_case_3() {
        // arrange
        let numbers: Vec<i32> = vec![
            51, 38, 73, 21, 27, 55, 18, 15, 79, 29, 13, 45, 8, -73, -92, -20, -50, -60, -70,
        ];
        let expected: i32 = 1;

        // act
        let actual = Solution::array_sign(numbers);

        // assert
        assert_eq!(expected, actual);
    }
}
