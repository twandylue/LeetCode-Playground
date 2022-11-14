pub struct Solution {}

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![1; nums.len()];
        let mut right = 1;
        let mut left = 1;

        for i in (0..nums.len()).rev() {
            res[i] = right;
            right *= nums[i];
        }

        for i in 0..nums.len() {
            res[i] *= left;
            left *= nums[i];
        }

        return res;
    }

    pub fn product_except_self2(nums: Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![1; nums.len()];
        let mut left: Vec<i32> = vec![1; nums.len()];
        let mut right: Vec<i32> = vec![1; nums.len()];
        let mut l = 1;
        let mut r = 1;

        for i in 0..nums.len() {
            left[i] = l;
            l *= nums[i];
        }

        for i in (0..nums.len()).rev() {
            right[i] = r;
            r *= nums[i];
        }

        for i in 0..nums.len() {
            res[i] = left[i] * right[i];
        }

        return res;
    }

    pub fn tests() {
        let input = vec![1, 2, 3, 4];
        let expected = vec![24, 12, 8, 6];
        let actual = Solution::product_except_self(input);

        assert_eq!(actual, expected);

        let input2 = vec![-1, 1, 0, -3, 3];
        let expected2 = vec![0, 0, 9, 0, 0];
        let actual2 = Solution::product_except_self(input2);

        assert_eq!(actual2, expected2);

        let input = vec![1, 2, 3, 4];
        let expected = vec![24, 12, 8, 6];
        let actual = Solution::product_except_self2(input);

        assert_eq!(actual, expected);

        let input2 = vec![-1, 1, 0, -3, 3];
        let expected2 = vec![0, 0, 9, 0, 0];
        let actual2 = Solution::product_except_self2(input2);

        assert_eq!(actual2, expected2);
    }
}
