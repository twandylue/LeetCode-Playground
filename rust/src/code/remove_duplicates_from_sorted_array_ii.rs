struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = 0;
        while r < nums.len() {
            let mut count: i32 = 1;
            while r < nums.len() - 1 && nums[r] == nums[r + 1] {
                count += 1;
                r += 1;
            }

            for _ in 0..std::cmp::min(2, count) {
                nums[l] = nums[r];
                l += 1;
            }

            r += 1;
        }

        l as i32
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_remove_duplicates_case_1() {
        // arrange
        let mut nums: Vec<i32> = vec![1, 1, 1, 2, 2, 3];
        let expected: i32 = 5;

        // act
        let actual = Solution::remove_duplicates(&mut nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_remove_duplicates_case_2() {
        // arrange
        let mut nums: Vec<i32> = vec![0, 0, 1, 1, 1, 1, 2, 3, 3];
        let expected: i32 = 7;

        // act
        let actual = Solution::remove_duplicates(&mut nums);

        // assert
        assert_eq!(actual, expected);
    }
}
