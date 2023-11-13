pub struct Solution {}

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        // NOTE: ref: https://ithelp.ithome.com.tw/articles/10213264
        if nums.len() < 3 || *nums.iter().min().unwrap() > 0 {
            return Vec::new();
        }

        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut numbers = nums.clone();
        numbers.sort_by(|a, b| a.cmp(b));

        for i in 0..numbers.len() - 2 {
            if i > 0 && numbers[i] == numbers[i - 1] {
                continue;
            }

            let mut j = i + 1;
            let mut k = numbers.len() - 1;
            while j < k {
                let t = numbers[i] + numbers[j] + numbers[k];
                if t > 0 {
                    k -= 1;
                } else if t < 0 {
                    j += 1;
                } else {
                    res.push(vec![numbers[i], numbers[j], numbers[k]]);
                    while j < k && numbers[j] == numbers[j + 1] {
                        j += 1;
                    }
                    while k > j && numbers[k] == numbers[k - 1] {
                        k -= 1;
                    }

                    j += 1;
                    k -= 1;
                }
            }
        }

        return res;
    }

    pub fn three_sum2(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        nums.sort();

        let mut prev_i: i32 = i32::MIN;
        for i in 0..nums.len() - 2 {
            if nums[i] == prev_i {
                continue;
            }
            let mut j = i + 1;
            let mut k = nums.len() - 1;
            while j < k {
                if nums[i] + nums[j] + nums[k] == 0 {
                    result.push(vec![nums[i], nums[j], nums[k]]);
                    let prev_j: i32 = nums[j];
                    while prev_j == nums[j] && j < k {
                        j += 1;
                    }
                } else if nums[i] + nums[j] + nums[k] < 0 {
                    j += 1;
                } else {
                    k -= 1;
                }
            }
            prev_i = nums[i];
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn three_sum_case_1() {
        let nums = vec![-1, 0, 1, 2, -1, -4];
        let expected = vec![vec![-1, -1, 2], vec![-1, 0, 1]];
        let actual = Solution::three_sum(nums);

        assert_eq!(actual, expected);
    }

    #[test]
    fn three_sum_case_2() {
        let nums2 = vec![0, 1, 1];
        let expected2: Vec<Vec<i32>> = Vec::new();
        let actual2 = Solution::three_sum(nums2);

        assert_eq!(actual2, expected2);
    }

    #[test]
    fn three_sum_case_3() {
        let nums3 = vec![0, 0, 0];
        let expected3 = vec![vec![0, 0, 0]];
        let actual3 = Solution::three_sum(nums3);

        assert_eq!(actual3, expected3);
    }

    #[test]
    fn three_sum_case_4() {
        let nums = vec![-1, 0, 1, 2, -1, -4];
        let expected = vec![vec![-1, -1, 2], vec![-1, 0, 1]];
        let actual = Solution::three_sum2(nums);

        assert_eq!(actual, expected);
    }

    #[test]
    fn three_sum_case_5() {
        let nums = vec![0, 1, 1];
        let expected: Vec<Vec<i32>> = Vec::new();
        let actual = Solution::three_sum2(nums);

        assert_eq!(actual, expected);
    }

    #[test]
    fn three_sum_case_6() {
        let nums = vec![0, 0, 0];
        let expected = vec![vec![0, 0, 0]];
        let actual = Solution::three_sum2(nums);

        assert_eq!(actual, expected);
    }

    #[test]
    fn three_sum_case_7() {
        let nums = vec![0, 0, 0, 0];
        let expected = vec![vec![0, 0, 0]];
        let actual = Solution::three_sum2(nums);

        assert_eq!(actual, expected);
    }
}
