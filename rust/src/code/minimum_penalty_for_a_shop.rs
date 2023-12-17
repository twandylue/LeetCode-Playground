struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn best_closing_time(customers: String) -> i32 {
        let customers: Vec<char> = customers.chars().collect();
        let mut ps1: Vec<i32> = vec![0; customers.len() + 1];
        let mut ps2: Vec<i32> = vec![0; customers.len() + 1];

        let mut penalty: i32 = 0;
        for i in 0..customers.len() {
            if customers[i] == 'N' {
                penalty += 1;
            }
            ps1[i + 1] = penalty;
        }

        penalty = 0;
        for i in (0..customers.len()).rev() {
            if customers[i] == 'Y' {
                penalty += 1;
            }
            ps2[i] = penalty;
        }

        let mut min_penalty: i32 = i32::MAX;
        let mut min_index: usize = 0;
        for i in 0..ps1.len() {
            if min_penalty > ps1[i] + ps2[i] {
                min_penalty = ps1[i] + ps2[i];
                min_index = i;
            }
        }

        return min_index as i32;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_best_closing_time_case_1() {
        // arrange
        let customers: String = "YYNY".to_string();
        let expected: i32 = 2;

        // act
        let actual = Solution::best_closing_time(customers);

        // assert
        assert_eq!(expected, actual);
    }
}
