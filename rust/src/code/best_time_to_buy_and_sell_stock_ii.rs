struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_price = 0;
        for i in 0..prices.len() - 1 {
            if prices[i + 1] < prices[i] {
                continue;
            }

            max_price += prices[i + 1] - prices[i];
        }

        max_price
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn max_profit_case_1() {
        // arrange
        let prices: Vec<i32> = vec![7, 1, 5, 3, 6, 4];
        let expected: i32 = 7;

        // act
        let actual = Solution::max_profit(prices);

        // assert
        assert_eq!(expected, actual);
    }
}
