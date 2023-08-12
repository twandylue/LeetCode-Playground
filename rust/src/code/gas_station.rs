struct Solution {}

impl Solution {
    // NOTE: time complexity O(n)
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        if gas.iter().sum::<i32>() < cost.iter().sum::<i32>() {
            return -1;
        }

        let mut start: i32 = 0;
        let mut total = 0;

        for i in 0..gas.len() {
            total += gas[i] - cost[i];
            if total < 0 {
                total = 0;
                start = i as i32 + 1;
            }
        }

        start
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_can_complete_circuit_case_1() {
        // arrange
        let gas = vec![1, 2, 3, 4, 5];
        let cost = vec![3, 4, 5, 1, 2];
        let expected = 3;

        // act
        let actual = Solution::can_complete_circuit(gas, cost);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_can_complete_circuit_case_2() {
        // arrange
        let gas = vec![2, 3, 4];
        let cost = vec![3, 4, 3];
        let expected = -1;

        // act
        let actual = Solution::can_complete_circuit(gas, cost);

        // assert
        assert_eq!(actual, expected);
    }
}
