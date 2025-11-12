struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        use std::collections::HashMap;

        let mut result: i32 = 0;
        let mut fruits_map: HashMap<i32, i32> = HashMap::new();
        let mut l: usize = 0;
        for r in 0..fruits.len() {
            fruits_map
                .entry(fruits[r])
                .and_modify(|x| *x += 1)
                .or_insert(1);
            let mut curr_len: i32 = (r - l + 1) as i32;

            while fruits_map.len() > 2 {
                fruits_map.entry(fruits[l]).and_modify(|x| *x -= 1);
                if let Some(n) = fruits_map.get(&fruits[l]) {
                    if *n == 0 {
                        fruits_map.remove(&fruits[l]);
                    }
                }
                l += 1;
                curr_len -= 1;
            }

            result = std::cmp::max(result, curr_len);
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_total_fruit_case_1() {
        // arrange
        let fruits: Vec<i32> = vec![1, 2, 1];
        let expected: i32 = 3;

        // act
        let actual = Solution::total_fruit(fruits);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_total_fruit_case_2() {
        // arrange
        let fruits: Vec<i32> = vec![0, 1, 2, 2];
        let expected: i32 = 3;

        // act
        let actual = Solution::total_fruit(fruits);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_total_fruit_case_3() {
        // arrange
        let fruits: Vec<i32> = vec![1, 2, 3, 2, 2];
        let expected: i32 = 4;

        // act
        let actual = Solution::total_fruit(fruits);

        // assert
        assert_eq!(expected, actual);
    }
}
