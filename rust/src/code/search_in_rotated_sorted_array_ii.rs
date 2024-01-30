struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        let mut l: usize = 0;
        let mut r: usize = nums.len() - 1;
        while l <= r {
            let mid: usize = (l + r) / 2;
            if nums[mid] == target {
                return true;
            }
            if nums[l] < nums[mid] {
                if nums[l] <= target && target < nums[mid] {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else if nums[l] > nums[mid] {
                if target > nums[mid] && target <= nums[r] {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            } else {
                l += 1;
            }
        }

        false
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_search_case_1() {
        // arrange
        let nums: Vec<i32> = vec![4, 5, 6, 7, 0, 1, 2];
        let target: i32 = 3;
        let expected: bool = false;

        // act
        let actual = Solution::search(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_search_case_2() {
        // arrange
        let nums: Vec<i32> = vec![4, 5, 6, 7, 0, 1, 2];
        let target: i32 = 0;
        let expected: bool = true;

        // act
        let actual = Solution::search(nums, target);

        // assert
        assert_eq!(expected, actual);
    }
}
