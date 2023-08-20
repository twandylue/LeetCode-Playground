struct Solution {}

impl Solution {
    // NOTE: time complexity O(n)
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut result = *nums.iter().max().unwrap();
        let mut max_num = 1;
        let mut min_num = 1;

        for n in nums {
            if n == 0 {
                max_num = 1;
                min_num = 1;
                continue;
            }

            let tmp = n * max_num;
            max_num = std::cmp::max(std::cmp::max(n * max_num, n * min_num), n);
            min_num = std::cmp::min(std::cmp::min(tmp, n * min_num), n);
            result = std::cmp::max(max_num, result);
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_product_case_1() {
        // arrange
        let nums = vec![2, 3, -2, 4];
        let expected = 6;

        // act
        let actual = Solution::max_product(nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_max_product_case_2() {
        // arrange
        let nums = vec![-2, 0, -1];
        let expected = 0;

        // act
        let actual = Solution::max_product(nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_max_product_case_3() {
        // arrange
        let nums = vec![-4, -3, -2];
        let expected = 12;

        // act
        let actual = Solution::max_product(nums);

        // assert
        assert_eq!(actual, expected);
    }
}
