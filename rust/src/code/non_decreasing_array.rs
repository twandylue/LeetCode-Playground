struct Solution {}

impl Solution {
    pub fn check_possibility(mut nums: Vec<i32>) -> bool {
        let mut count: i32 = 0;
        for i in 0..nums.len() - 1 {
            if nums[i] <= nums[i + 1] {
                continue;
            }
            if count >= 1 {
                return false;
            }
            if i == 0 || nums[i - 1] <= nums[i + 1] {
                // [3,5,4,2]
                nums[i] = nums[i + 1];
            } else {
                // [4,5,3,2]
                nums[i + 1] = nums[i];
            }
            count += 1;
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn check_possibility_case_1() {
        // arrange
        let nums: Vec<i32> = vec![4, 2, 3];
        let expected: bool = true;

        // act
        let actual = Solution::check_possibility(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn check_possibility_case_2() {
        // arrange
        let nums: Vec<i32> = vec![4, 2, 1];
        let expected: bool = false;

        // act
        let actual = Solution::check_possibility(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn check_possibility_case_3() {
        // arrange
        let nums: Vec<i32> = vec![4, 3, 2, 5];
        let expected: bool = false;

        // act
        let actual = Solution::check_possibility(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
