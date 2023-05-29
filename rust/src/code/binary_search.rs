pub struct Solution {}

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut l = 0;
        let mut r = nums.len() - 1;
        while l <= r {
            let m = (l + r) / 2;
            if nums[m] == target {
                return m as i32;
            } else if nums[m] > target {
                if m == 0 {
                    break;
                }
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        -1
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn binary_search_case_1() {
        // arrange
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 9;
        let expected = 4;

        // act
        let actual = Solution::search(nums, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn binary_search_case_2() {
        // arrange
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 2;
        let expected = -1;

        // act
        let actual = Solution::search(nums, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn binary_search_case_3() {
        // arrange
        let nums = vec![5];
        let target = -5;
        let expected = -1;

        // act
        let actual = Solution::search(nums, target);

        // assert
        assert_eq!(actual, expected);
    }
}
