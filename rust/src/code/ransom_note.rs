struct Solution;

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut r_count: Vec<i32> = vec![0; 26];
        let mut m_count: Vec<i32> = vec![0; 26];
        for c in magazine.chars() {
            m_count[c as usize - 'a' as usize] += 1;
        }
        for c in ransom_note.chars() {
            let i: usize = c as usize - 'a' as usize;
            r_count[i] += 1;
            if m_count[i] == 0 || r_count[i] > m_count[i] {
                return false;
            }
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_can_construct_case_1() {
        // arrange
        let ransom_note: String = "a".to_string();
        let magazine: String = "b".to_string();
        let expected: bool = false;

        // act
        let actual = Solution::can_construct(ransom_note, magazine);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_construct_case_2() {
        // arrange
        let ransom_note: String = "aa".to_string();
        let magazine: String = "ab".to_string();
        let expected: bool = false;

        // act
        let actual = Solution::can_construct(ransom_note, magazine);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_construct_case_3() {
        // arrange
        let ransom_note: String = "aa".to_string();
        let magazine: String = "aab".to_string();
        let expected: bool = true;

        // act
        let actual = Solution::can_construct(ransom_note, magazine);

        // assert
        assert_eq!(expected, actual);
    }
}
