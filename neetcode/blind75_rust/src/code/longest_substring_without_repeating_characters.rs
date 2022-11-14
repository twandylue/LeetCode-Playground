use std::{cmp, collections::HashSet};

pub struct Solution {}

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut res = 0;
        let mut count = 0;
        let mut i = 0;
        let mut j = 0;
        let mut set: HashSet<char> = HashSet::new();
        let chars: Vec<char> = s.chars().collect();

        while j < chars.len() {
            if !set.contains(&chars[j]) {
                set.insert(chars[j]);
                count += 1;
            } else {
                while chars[i] != chars[j] {
                    set.remove(&chars[i]);
                    count -= 1;
                    i += 1;
                }
                i += 1;
            }

            res = cmp::max(res, count);
            j += 1;
        }

        return res;
    }

    pub fn tests() {
        let s = String::from("abcabcbb");
        let expected = 3;
        let actual = Solution::length_of_longest_substring(s);

        assert_eq!(actual, expected);

        let s2 = String::from("bbbbb");
        let expected2 = 1;
        let actual2 = Solution::length_of_longest_substring(s2);

        assert_eq!(actual2, expected2);

        let s3 = String::from("pwwkew");
        let expected3 = 3;
        let actual3 = Solution::length_of_longest_substring(s3);

        assert_eq!(actual3, expected3);
    }
}
