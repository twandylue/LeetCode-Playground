struct Solution {}

impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = nums.len() - 1;
        let mut mid: usize = 0;
        while l <= r {
            mid = (l + r) / 2;
            if mid < nums.len() - 1 && nums[mid] < nums[mid + 1] {
                l = mid + 1;
            } else if mid > 0 && nums[mid] < nums[mid - 1] {
                r = mid - 1;
            } else {
                return mid as i32;
            }
        }
        mid as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_peak_element_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3, 1];
        let expected: i32 = 2;

        // act
        let actual = Solution::find_peak_element(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_peak_element_case_2() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 1, 3, 5, 6, 4];
        let expected: i32 = 5;

        // act
        let actual = Solution::find_peak_element(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
