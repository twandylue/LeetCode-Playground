struct Solution {}

impl Solution {
    // NOTE: time complexity O(n * m) where n is amount and m is coins length
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut dp: Vec<i32> = vec![amount + 1; amount as usize + 1];
        dp[0] = 0;

        for i in 1..(amount + 1) {
            for c in coins.iter() {
                if i - c >= 0 {
                    dp[i as usize] = std::cmp::min(dp[i as usize], 1 + dp[(i - c) as usize]);
                }
            }
        }

        return if dp[amount as usize] == amount + 1 {
            -1
        } else {
            dp[amount as usize]
        };
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_coin_change_case_1() {
        // arrange
        let coins = vec![1, 2, 5];
        let amount = 11;
        let expected = 3;

        // act
        let result = Solution::coin_change(coins, amount);

        // assert
        assert_eq!(result, expected);
    }

    #[test]
    fn test_coin_change_case_2() {
        // arrange
        let coins = vec![2];
        let amount = 3;
        let expected = -1;

        // act
        let result = Solution::coin_change(coins, amount);

        // assert
        assert_eq!(result, expected);
    }

    #[test]
    fn test_coin_change_case_3() {
        // arrange
        let coins = vec![1];
        let amount = 0;
        let expected = 0;

        // act
        let result = Solution::coin_change(coins, amount);

        // assert
        assert_eq!(result, expected);
    }
}
