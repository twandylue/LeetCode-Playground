use std::cmp;

pub struct Solution {}

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut ret = 0;
        let mut i = 0;
        let mut j = height.len() - 1;

        while i < j {
            let area = (j - i) as i32 * cmp::min(height[j], height[i]);
            ret = cmp::max(ret, area);

            if height[i] < height[j] {
                i += 1;
            } else {
                j -= 1;
            }
        }

        return ret as i32;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let height = vec![1, 8, 6, 2, 5, 4, 8, 3, 7];
        let expected = 49;
        let actual = Solution::max_area(height);

        assert_eq!(actual, expected);

        let height2 = vec![1, 1];
        let expected2 = 1;
        let actual2 = Solution::max_area(height2);

        assert_eq!(actual2, expected2);
    }
}
