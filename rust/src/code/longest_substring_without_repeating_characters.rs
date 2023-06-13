use std::{cmp, collections::HashSet};

pub struct Solution {}

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut max_len = 0;
        let mut l = 0;
        let mut r = 0;
        let mut set: HashSet<char> = HashSet::new();
        let chars: Vec<char> = s.chars().collect();

        while r < chars.len() {
            if set.contains(&chars[r]) {
                set.remove(&chars[l]);
                l += 1;
            } else {
                set.insert(chars[r]);
                max_len = cmp::max(max_len, set.len());
                r += 1;
            }
        }

        return max_len as i32;
    }

    pub fn length_of_longest_substring_2(s: String) -> i32 {
        let mut l = 0;
        let mut max_len = 0;
        let mut set: HashSet<char> = HashSet::new();
        let chars: Vec<char> = s.chars().collect();

        for r in 0..chars.len() {
            while set.contains(&chars[r]) {
                set.remove(&chars[l]);
                l += 1;
            }

            set.insert(chars[r]);
            max_len = cmp::max(max_len, set.len());
        }

        return max_len as i32;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn length_of_longest_substring_case_1() {
        // arrange
        let s = String::from("abcabcbb");
        let expected = 3;

        // act
        let actual = Solution::length_of_longest_substring(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn length_of_longest_substring_case_2() {
        // arrange
        let s = String::from("bbbbb");
        let expected = 1;

        // act
        let actual = Solution::length_of_longest_substring(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn length_of_longest_substring_case_3() {
        // arrange
        let s = String::from("pwwkew");
        let expected3 = 3;

        // act
        let actual = Solution::length_of_longest_substring(s);

        // assert
        assert_eq!(actual, expected3);
    }

    #[test]
    fn length_of_longest_substring_case_4() {
        // arrange
        let s = String::from("aabaab!bb");
        let expected = 3;

        // act
        let actual = Solution::length_of_longest_substring(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn length_of_longest_substring_case_5() {
        // arrange
        let s = String::from("abcabcbb");
        let expected = 3;

        // act
        let actual = Solution::length_of_longest_substring_2(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn length_of_longest_substring_case_6() {
        // arrange
        let s = String::from("bbbbb");
        let expected = 1;

        // act
        let actual = Solution::length_of_longest_substring_2(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn length_of_longest_substring_case_7() {
        // arrange
        let s = String::from("pwwkew");
        let expected = 3;

        // act
        let actual = Solution::length_of_longest_substring_2(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn length_of_longest_substring_case_8() {
        // arrange
        let s = String::from("aabaab!bb");
        let expected = 3;

        // act
        let actual = Solution::length_of_longest_substring_2(s);

        // assert
        assert_eq!(actual, expected);
    }
}
