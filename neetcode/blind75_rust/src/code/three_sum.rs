// ref: https://ithelp.ithome.com.tw/articles/10213264

pub struct Solution {}

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
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
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums = vec![-1, 0, 1, 2, -1, -4];
        let expected = vec![vec![-1, -1, 2], vec![-1, 0, 1]];
        let actual = Solution::three_sum(nums);

        assert_eq!(actual, expected);
    }

    #[test]
    fn case_2() {
        let nums2 = vec![0, 1, 1];
        let expected2: Vec<Vec<i32>> = Vec::new();
        let actual2 = Solution::three_sum(nums2);

        assert_eq!(actual2, expected2);
    }

    #[test]
    fn case_3() {
        let nums3 = vec![0, 0, 0];
        let expected3 = vec![vec![0, 0, 0]];
        let actual3 = Solution::three_sum(nums3);

        assert_eq!(actual3, expected3);
    }
}
