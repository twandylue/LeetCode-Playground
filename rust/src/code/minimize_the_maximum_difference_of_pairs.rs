struct Solution {}

impl Solution {
    // NOTE: time complexity: O(nlogn)
    pub fn minimize_max(mut nums: Vec<i32>, p: i32) -> i32 {
        nums.sort();
        let mut l: i32 = 0;
        let mut r: i32 = 10_i32.pow(9);
        let mut result: i32 = r;
        while l <= r {
            let mid = (l + r) / 2;
            if Self::is_valid(mid, &nums, p) {
                result = mid;
                if mid.checked_sub(1).is_none() {
                    break;
                }
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        result
    }

    fn is_valid(diff: i32, nums: &Vec<i32>, p: i32) -> bool {
        let mut i: usize = 0;
        let mut count: i32 = 0;
        while i < nums.len() - 1 {
            if nums[i + 1] - nums[i] <= diff {
                i += 2;
                count += 1;
            } else {
                i += 1;
            }
        }
        count >= p
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_minimize_max_case_1() {
        // arrange
        let nums: Vec<i32> = vec![10, 1, 2, 7, 1, 3];
        let p: i32 = 2;
        let expected: i32 = 1;

        // act
        let actual = Solution::minimize_max(nums, p);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_minimize_max_case_2() {
        // arrange
        let nums: Vec<i32> = vec![4, 2, 1, 2];
        let p: i32 = 1;
        let expected: i32 = 0;

        // act
        let actual = Solution::minimize_max(nums, p);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_minimize_max_case_3() {
        // arrange
        let nums: Vec<i32> = vec![0, 5, 3, 4];
        let p: i32 = 0;
        let expected: i32 = 0;

        // act
        let actual = Solution::minimize_max(nums, p);

        // assert
        assert_eq!(expected, actual);
    }
}
