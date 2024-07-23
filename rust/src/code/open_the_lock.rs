struct Solution {}

use std::collections::{HashSet, VecDeque};

impl Solution {
    // NOTE: time complexity O(n) where n is the number of nodes
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        if deadends.contains(&"0000".to_string()) {
            return -1;
        }
        let mut visited: HashSet<String> = HashSet::new();
        for end in deadends {
            visited.insert(end);
        }
        let mut queue: VecDeque<(String, i32)> = VecDeque::from([("0000".to_string(), 0)]);
        while let Some((lock, turns)) = queue.pop_front() {
            if lock == target {
                return turns;
            }
            for neighbor in Self::children(lock.chars().collect()) {
                if visited.contains(&neighbor) {
                    continue;
                }
                visited.insert(neighbor.clone());
                queue.push_back((neighbor.clone(), turns + 1));
            }
        }
        -1
    }

    fn children(mut lock: Vec<char>) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        for i in 0..4 {
            let original_digit: char = lock[i];
            let mut digit: char = std::char::from_digit(
                ((original_digit.to_digit(10).unwrap() as i32 + 1) % 10) as u32,
                10,
            )
            .unwrap();
            let mut result_1: Vec<char> = lock.clone();
            result_1[i] = digit;
            result.push(result_1.iter().collect());
            digit = std::char::from_digit(
                ((original_digit.to_digit(10).unwrap() as i32 - 1 + 10) % 10) as u32,
                10,
            )
            .unwrap();
            let mut result_2: Vec<char> = lock.clone();
            result_2[i] = digit;
            result.push(result_2.iter().collect());
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_open_lock_case_1() {
        // arrange
        let deadends: Vec<String> = vec![
            "0201".to_string(),
            "0101".to_string(),
            "0102".to_string(),
            "1212".to_string(),
            "2002".to_string(),
        ];
        let target: String = "0202".to_string();
        let expected: i32 = 6;

        // act
        let actual = Solution::open_lock(deadends, target);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_open_lock_case_2() {
        // arrange
        let deadends: Vec<String> = vec!["8888".to_string()];
        let target: String = "0009".to_string();
        let expected: i32 = 1;

        // act
        let actual = Solution::open_lock(deadends, target);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_open_lock_case_3() {
        // arrange
        let deadends: Vec<String> = vec![
            "8887".to_string(),
            "8889".to_string(),
            "8878".to_string(),
            "8898".to_string(),
            "8788".to_string(),
            "8988".to_string(),
            "7888".to_string(),
            "9888".to_string(),
        ];
        let target: String = "8888".to_string();
        let expected: i32 = -1;

        // act
        let actual = Solution::open_lock(deadends, target);

        // arrange
        assert_eq!(expected, actual);
    }
}
