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
    fn case_1() {
        let s = String::from("abcabcbb");
        let expected = 3;
        let actual = Solution::length_of_longest_substring(s);

        assert_eq!(actual, expected);
    }

    #[test]
    fn case_2() {
        let s = String::from("bbbbb");
        let expected = 1;
        let actual = Solution::length_of_longest_substring(s);

        assert_eq!(actual, expected);
    }

    #[test]
    fn case_3() {
        let s = String::from("pwwkew");
        let expected3 = 3;
        let actual = Solution::length_of_longest_substring(s);

        assert_eq!(actual, expected3);
    }

    #[test]
    fn case_4() {
        let s = String::from("aabaab!bb");
        let expected = 3;
        let actual = Solution::length_of_longest_substring(s);

        assert_eq!(actual, expected);
    }

    #[test]
    fn case_5() {
        let s = String::from("abcabcbb");
        let expected = 3;
        let actual = Solution::length_of_longest_substring_2(s);

        assert_eq!(actual, expected);
    }

    #[test]
    fn case_6() {
        let s = String::from("bbbbb");
        let expected = 1;
        let actual = Solution::length_of_longest_substring_2(s);

        assert_eq!(actual, expected);
    }

    #[test]
    fn case_7() {
        let s = String::from("pwwkew");
        let expected = 3;
        let actual = Solution::length_of_longest_substring_2(s);

        assert_eq!(actual, expected);
    }

    #[test]
    fn case_8() {
        let s = String::from("aabaab!bb");
        let expected = 3;
        let actual = Solution::length_of_longest_substring_2(s);

        assert_eq!(actual, expected);
    }
}
