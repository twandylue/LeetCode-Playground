struct Solution {}

impl Solution {
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = nums.len() - 1;
        let mut result: usize = 0;
        while l <= r {
            let mid: usize = (l + r) / 2;
            result = mid;
            if mid > 0
                && nums[mid] != nums[mid - 1]
                && mid < nums.len() - 1
                && nums[mid] != nums[mid + 1]
            {
                return nums[mid];
            }

            let left_size: usize = if mid < nums.len() - 1 && nums[mid] == nums[mid + 1] {
                mid
            } else {
                mid + 1
            };

            if left_size % 2 == 0 {
                l = mid + 1;
            } else {
                if mid.checked_sub(1).is_none() {
                    break;
                }
                r = mid - 1;
            }
        }

        nums[result]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_single_non_duplicate_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 1, 2, 3, 3, 4, 4, 8, 8];
        let expected: i32 = 2;

        // act
        let actual = Solution::single_non_duplicate(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_single_non_duplicate_case_2() {
        // arrange
        let nums: Vec<i32> = vec![3, 3, 7, 7, 10, 11, 11];
        let expected: i32 = 10;

        // act
        let actual = Solution::single_non_duplicate(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_single_non_duplicate_case_3() {
        // arrange
        let nums: Vec<i32> = vec![3, 3, 7, 7, 10];
        let expected: i32 = 10;

        // act
        let actual = Solution::single_non_duplicate(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_single_non_duplicate_case_4() {
        // arrange
        let nums: Vec<i32> = vec![1, 3, 3, 7, 7];
        let expected: i32 = 1;

        // act
        let actual = Solution::single_non_duplicate(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
