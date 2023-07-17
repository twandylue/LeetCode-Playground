use std::collections::HashMap;

struct Solution {}

// NOTE: time complexity: O(4^n)
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        let mut subset: Vec<char> = Vec::new();
        let digit_to_char: HashMap<char, Vec<char>> = HashMap::from([
            ('2', vec!['a', 'b', 'c']),
            ('3', vec!['d', 'e', 'f']),
            ('4', vec!['g', 'h', 'i']),
            ('5', vec!['j', 'k', 'l']),
            ('6', vec!['m', 'n', 'o']),
            ('7', vec!['p', 'q', 'r', 's']),
            ('8', vec!['t', 'u', 'v']),
            ('9', vec!['w', 'x', 'y', 'z']),
        ]);

        if !digits.is_empty() {
            Self::dfs(0, &digit_to_char, &digits, &mut subset, &mut result);
        }

        result
    }

    fn dfs(
        pos: usize,
        digit_to_char: &HashMap<char, Vec<char>>,
        digits: &str,
        subset: &mut Vec<char>,
        result: &mut Vec<String>,
    ) {
        if subset.len() == digits.len() {
            result.push(subset.iter().collect::<String>());
            return;
        }

        if let Some(d) = digits.chars().nth(pos) {
            for c in digit_to_char[&d].iter() {
                subset.push(*c);
                Self::dfs(pos + 1, digit_to_char, digits, subset, result);
                subset.pop().unwrap();
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn letter_combinations_case_1() {
        // arrange
        let digits: String = "23".to_string();
        let expected: Vec<String> = vec![
            "ad".to_string(),
            "ae".to_string(),
            "af".to_string(),
            "bd".to_string(),
            "be".to_string(),
            "bf".to_string(),
            "cd".to_string(),
            "ce".to_string(),
            "cf".to_string(),
        ];

        // act
        let actual = Solution::letter_combinations(digits);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn letter_combinations_case_2() {
        // arrange
        let digits: String = "".to_string();
        let expected: Vec<String> = vec![];

        // act
        let actual = Solution::letter_combinations(digits);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn letter_combinations_case_3() {
        // arrange
        let digits: String = "2".to_string();
        let expected: Vec<String> = vec!["a".to_string(), "b".to_string(), "c".to_string()];

        // act
        let actual = Solution::letter_combinations(digits);

        // assert
        assert_eq!(expected, actual);
    }
}
