use std::cmp;

pub struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ret = 0;
        let mut curr = 0;

        for i in 0..prices.len() - 1 {
            curr = prices[i + 1] - prices[i] + curr;
            curr = cmp::max(curr, 0);
            ret = cmp::max(curr, ret);
        }

        return ret;
    }

    pub fn max_profit2(prices: Vec<i32>) -> i32 {
        let mut ret = 0;
        let mut i = 0;
        let mut j = 0;

        while j < prices.len() {
            if prices[j] > prices[i] {
                ret = cmp::max(ret, prices[j] - prices[i]);
            } else {
                i = j;
            }
            j += 1
        }

        return ret;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let prices = vec![7, 1, 5, 3, 6, 4];
        let expected = 5;
        let actual = Solution::max_profit(prices);

        assert_eq!(actual, expected);

        let prices2 = vec![7, 6, 4, 3, 1];
        let expected2 = 0;
        let actual2 = Solution::max_profit(prices2);

        assert_eq!(actual2, expected2);

        let prices = vec![7, 1, 5, 3, 6, 4];
        let expected = 5;
        let actual = Solution::max_profit2(prices);

        assert_eq!(actual, expected);

        let prices2 = vec![7, 6, 4, 3, 1];
        let expected2 = 0;
        let actual2 = Solution::max_profit2(prices2);

        assert_eq!(actual2, expected2);
    }
}
