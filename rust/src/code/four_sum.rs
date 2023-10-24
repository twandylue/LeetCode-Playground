struct Solution {}

impl Solution {
    pub fn four_sum(mut nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        if nums.len() < 4 {
            return Vec::new();
        }

        nums.sort();
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut prev_i: i32 = i32::MIN;
        for i in 0..nums.len() - 3 {
            if prev_i == nums[i] {
                continue;
            }
            let mut prev_j: i32 = i32::MIN;
            for j in i + 1..nums.len() - 2 {
                if prev_j == nums[j] {
                    continue;
                }
                let mut k: usize = j + 1;
                let mut e: usize = nums.len() - 1;
                let mut prev_k: i32 = i32::MIN;
                while k < e {
                    let sum: i64 =
                        nums[i] as i64 + nums[j] as i64 + nums[k] as i64 + nums[e] as i64;
                    let target: i64 = target as i64;
                    if sum == target {
                        result.push(vec![nums[i], nums[j], nums[k], nums[e]]);
                        prev_k = nums[k];
                        while prev_k == nums[k] && k < e {
                            prev_k = nums[k];
                            k += 1;
                        }
                    } else if sum > target {
                        e -= 1;
                    } else {
                        k += 1;
                    }
                }
                prev_j = nums[j];
            }
            prev_i = nums[i];
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn four_sum_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 0, -1, 0, -2, 2];
        let target: i32 = 0;
        let expected: Vec<Vec<i32>> =
            vec![vec![-2, -1, 1, 2], vec![-2, 0, 0, 2], vec![-1, 0, 0, 1]];

        // act
        let actual = Solution::four_sum(nums, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn four_sum_case_2() {
        // arrange
        let nums: Vec<i32> = vec![2, 2, 2, 2, 2];
        let target: i32 = 8;
        let expected: Vec<Vec<i32>> = vec![vec![2, 2, 2, 2]];

        // act
        let actual = Solution::four_sum(nums, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn four_sum_case_3() {
        // arrange
        let nums: Vec<i32> = vec![0];
        let target: i32 = 0;
        let expected: Vec<Vec<i32>> = vec![];

        // act
        let actual = Solution::four_sum(nums, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn four_sum_case_4() {
        // arrange
        let nums: Vec<i32> = vec![1000000000, 1000000000, 1000000000, 1000000000];
        let target: i32 = -294967296;
        let expected: Vec<Vec<i32>> = vec![];

        // act
        let actual = Solution::four_sum(nums, target);

        // assert
        assert_eq!(actual, expected);
    }
}
