struct Solution {}

impl Solution {
    // NOTE: time complexity O(E * K)
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let mut prices: Vec<i32> = vec![std::i32::MAX; n as usize];
        prices[src as usize] = 0;

        for _ in 0..(k + 1) {
            let mut tmp_prices: Vec<i32> = prices.clone();
            for flight in flights.iter() {
                let s: i32 = flight[0];
                let d: i32 = flight[1];
                let p: i32 = flight[2];
                if prices[s as usize] == std::i32::MAX {
                    continue;
                }
                if prices[s as usize] + p < tmp_prices[d as usize] {
                    tmp_prices[d as usize] = prices[s as usize] + p;
                }
            }
            prices = tmp_prices;
        }

        return if prices[dst as usize] == std::i32::MAX {
            -1
        } else {
            prices[dst as usize]
        };
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn find_cheapest_price_case_1() {
        // arrange
        let n = 4;
        let flights: Vec<Vec<i32>> = vec![
            vec![0, 1, 100],
            vec![1, 2, 100],
            vec![2, 0, 100],
            vec![1, 3, 600],
            vec![2, 3, 200],
        ];
        let src = 0;
        let dst = 3;
        let k = 1;
        let expected: i32 = 700;

        // act
        let actual = Solution::find_cheapest_price(n, flights, src, dst, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn find_cheapest_price_case_2() {
        // arrange
        let n = 3;
        let flights: Vec<Vec<i32>> = vec![vec![0, 1, 100], vec![1, 2, 100], vec![0, 2, 500]];
        let src = 0;
        let dst = 2;
        let k = 1;
        let expected: i32 = 200;

        // act
        let actual = Solution::find_cheapest_price(n, flights, src, dst, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn find_cheapest_price_case_3() {
        // arrange
        let n = 3;
        let flights: Vec<Vec<i32>> = vec![vec![0, 1, 100], vec![1, 2, 100], vec![0, 2, 500]];
        let src = 0;
        let dst = 2;
        let k = 0;
        let expected: i32 = 500;

        // act
        let actual = Solution::find_cheapest_price(n, flights, src, dst, k);

        // assert
        assert_eq!(expected, actual);
    }
}
