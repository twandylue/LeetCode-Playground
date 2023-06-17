struct Solution {}

impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut output: Vec<i32> = vec![-1, -1];
        if nums.len() == 0 {
            return output;
        }
        let mut l: usize = 0;
        let mut r: usize = nums.len() - 1;

        // NOTE: for left part
        while l <= r && r < nums.len() {
            let mid = (l + r) / 2;
            if nums[mid] == target {
                output[0] = mid as i32;
                if mid > 0 {
                    r = mid - 1;
                    l = 0;
                } else {
                    break;
                }
            } else if nums[mid] < target {
                l = mid + 1;
            } else if nums[mid] > target {
                if mid > 0 {
                    r = mid - 1;
                } else {
                    break;
                }
            }
        }

        l = 0;
        r = nums.len() - 1;
        // NOTE: for right part
        while l <= r && r < nums.len() {
            let mid = (l + r) / 2;
            if nums[mid] == target {
                output[1] = mid as i32;
                l = mid + 1;
                r = nums.len() - 1;
            } else if nums[mid] < target {
                l = mid + 1;
            } else if nums[mid] > target {
                if mid > 0 {
                    r = mid - 1;
                } else {
                    break;
                }
            }
        }

        return output;
    }

    pub fn search_range_2(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let left = Self::binary_search(&nums, target, true);
        let right = Self::binary_search(&nums, target, false);

        return vec![left, right];
    }

    fn binary_search(nums: &Vec<i32>, target: i32, left_bias: bool) -> i32 {
        let mut output: i32 = -1;

        if nums.is_empty() {
            return output;
        }
        let mut l = 0;
        let mut r = nums.len() - 1;

        while l <= r && r < nums.len() {
            let mid = (l + r) / 2;
            if nums[mid] == target {
                output = mid as i32;
                if left_bias {
                    if mid > 0 {
                        r = mid - 1;
                        l = 0;
                    } else {
                        break;
                    }
                } else {
                    l = mid + 1;
                    r = nums.len() - 1;
                }
            } else if nums[mid] < target {
                l = mid + 1;
            } else {
                if mid > 0 {
                    r = mid - 1;
                } else {
                    break;
                }
            }
        }

        return output;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn search_range_case_1() {
        // arrange
        let nums = vec![5, 7, 7, 8, 8, 10];
        let target = 8;
        let expected = vec![3, 4];

        // act
        let actual = Solution::search_range(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_range_case_2() {
        // arrange
        let nums = vec![5, 7, 7, 8, 8, 10];
        let target = 6;
        let expected = vec![-1, -1];

        // act
        let actual = Solution::search_range(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_range_case_3() {
        // arrange
        let nums = vec![];
        let target = 0;
        let expected = vec![-1, -1];

        // act
        let actual = Solution::search_range(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_range_2_case_1() {
        // arrange
        let nums = vec![5, 7, 7, 8, 8, 10];
        let target = 8;
        let expected = vec![3, 4];

        // act
        let actual = Solution::search_range_2(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_range_2_case_2() {
        // arrange
        let nums = vec![5, 7, 7, 8, 8, 10];
        let target = 6;
        let expected = vec![-1, -1];

        // act
        let actual = Solution::search_range_2(nums, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_range_2_case_3() {
        // arrange
        let nums = vec![];
        let target = 0;
        let expected = vec![-1, -1];

        // act
        let actual = Solution::search_range_2(nums, target);

        // assert
        assert_eq!(expected, actual);
    }
}
