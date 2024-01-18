struct Solution {}

impl Solution {
    // NOTE: time complexity: O(logn)
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut mid: usize = 0;
        let mut l: usize = 0;
        let mut r: usize = nums.len() - 1;
        while l <= r {
            mid = (l + r) / 2;
            if nums[mid] == target {
                return mid as i32;
            } else if nums[mid] > target {
                if mid > 0 && target > nums[mid - 1] {
                    return mid as i32;
                }

                if mid.checked_sub(1).is_none() {
                    break;
                }
                r = mid - 1;
            } else {
                if mid < nums.len() - 1 && target < nums[mid + 1] {
                    return mid as i32 + 1;
                }
                l = mid + 1;
            }
        }

        return if mid == 0 && nums[0] > target {
            0
        } else {
            mid as i32 + 1
        };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_search_insert_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 3, 5, 6];
        let target: i32 = 5;
        let expected: i32 = 2;

        // act
        let actual = Solution::search_insert(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_search_insert_case_2() {
        // arrange
        let nums: Vec<i32> = vec![1, 3, 5, 6];
        let target: i32 = 2;
        let expected: i32 = 1;

        // act
        let actual = Solution::search_insert(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_search_insert_case_3() {
        // arrange
        let nums: Vec<i32> = vec![1, 3, 5, 6];
        let target: i32 = 7;
        let expected: i32 = 4;

        // act
        let actual = Solution::search_insert(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_search_insert_case_4() {
        // arrange
        let nums: Vec<i32> = vec![1, 3];
        let target: i32 = 0;
        let expected: i32 = 0;

        // act
        let actual = Solution::search_insert(nums, target);

        // assert
        assert_eq!(expected, actual);
    }
}
