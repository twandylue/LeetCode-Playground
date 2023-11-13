use std::collections::{HashMap, HashSet};

struct Solution {}

impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut result: HashSet<(char, char)> = HashSet::new();
        let mut left: HashSet<char> = HashSet::new();
        let mut right: HashMap<char, i32> = HashMap::new();

        for c in s.iter() {
            right.entry(*c).and_modify(|x| *x += 1).or_insert(1);
        }

        for i in 0..s.len() {
            right.entry(s[i]).and_modify(|x| *x -= 1);
            if let Some(&count) = right.get(&s[i]) {
                if count <= 0 {
                    let _ = right.remove(&s[i]);
                }
            }

            for j in 0..26 {
                let left_char: char = ('a' as u8 + j as u8) as char;
                if left.contains(&left_char) && right.contains_key(&left_char) {
                    result.insert((left_char, s[i]));
                }
            }

            left.insert(s[i]);
        }

        return result.len() as i32;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_palindromic_subsequence_case_1() {
        // arrange
        let s: String = "aabca".to_string();
        let expected: i32 = 3;

        // act
        let actual = Solution::count_palindromic_subsequence(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_count_palindromic_subsequence_case_2() {
        // arrange
        let s: String = "adc".to_string();
        let expected: i32 = 0;

        // act
        let actual = Solution::count_palindromic_subsequence(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_count_palindromic_subsequence_case_3() {
        // arrange
        let s: String = "bbcbaba".to_string();
        let expected: i32 = 4;

        // act
        let actual = Solution::count_palindromic_subsequence(s);

        // assert
        assert_eq!(expected, actual);
    }
}
