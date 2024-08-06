struct Solution;

impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        for word in words {
            let word: Vec<char> = word.chars().collect();
            if Self::is_pali(&word) {
                return word.iter().collect::<String>();
            }
        }
        "".to_string()
    }

    fn is_pali(word: &Vec<char>) -> bool {
        if word.len() == 0 {
            return true;
        }
        let mut i: usize = 0;
        let mut j: usize = word.len() - 1;
        while i < j {
            if word[i] != word[j] {
                return false;
            }
            i += 1;
            j -= 1;
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_first_palindrome_case_1() {
        // arrange
        let words: Vec<String> = vec![
            "abc".to_string(),
            "car".to_string(),
            "ada".to_string(),
            "racecar".to_string(),
            "cool".to_string(),
        ];
        let expected: String = "ada".to_string();

        // act
        let actual = Solution::first_palindrome(words);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_first_palindrome_case_2() {
        // arrange
        let words: Vec<String> = vec!["notapalindrome".to_string(), "racecar".to_string()];
        let expected: String = "racecar".to_string();

        // act
        let actual = Solution::first_palindrome(words);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_first_palindrome_case_3() {
        // arrange
        let words: Vec<String> = vec!["def".to_string(), "ghi".to_string()];
        let expected: String = "".to_string();

        // act
        let actual = Solution::first_palindrome(words);

        // assert
        assert_eq!(expected, actual);
    }
}
