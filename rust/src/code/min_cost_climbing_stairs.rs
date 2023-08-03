use std::cmp::min;

struct Solution {}

impl Solution {
    pub fn min_cost_climbing_stairs(mut cost: Vec<i32>) -> i32 {
        cost.push(0);
        for i in (0..cost.len() - 3).rev() {
            cost[i] += min(cost[i + 1], cost[i + 2]);
        }

        return min(cost[0], cost[1]);
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn min_cost_climbing_stairs_case_1() {
        // arrange
        let cost: Vec<i32> = vec![10, 15, 20];
        let expected: i32 = 15;

        // act
        let actual = Solution::min_cost_climbing_stairs(cost);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn min_cost_climbing_stairs_case_2() {
        // arrange
        let cost: Vec<i32> = vec![1, 100, 1, 1, 1, 100, 1, 1, 100, 1];
        let expected: i32 = 6;

        // act
        let actual = Solution::min_cost_climbing_stairs(cost);

        // assert
        assert_eq!(expected, actual);
    }
}
