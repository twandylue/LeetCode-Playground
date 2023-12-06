struct Solution {}

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut result = 0;
        let mut r: usize = s.len() - 1;
        while r >= 0 {
            if !s[r].is_whitespace() {
                let mut l: usize = r;
                while l >= 0 && !s[l].is_whitespace() {
                    result += 1;
                    if l.checked_sub(1).is_none() {
                        break;
                    }
                    l -= 1;
                }
                break;
            }
            if r.checked_sub(1).is_none() {
                break;
            }
            r -= 1;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn length_of_last_word_case_1() {
        // arrange
        let s: String = "Hello World".to_string();
        let expected: i32 = 5;

        // act
        let actual = Solution::length_of_last_word(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn length_of_last_word_case_2() {
        // arrange
        let s: String = "   fly me   to   the moon  ".to_string();
        let expected: i32 = 4;

        // act
        let actual = Solution::length_of_last_word(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn length_of_last_word_case_3() {
        // arrange
        let s: String = "a".to_string();
        let expected: i32 = 1;

        // act
        let actual = Solution::length_of_last_word(s);

        // assert
        assert_eq!(expected, actual);
    }
}
