use std::{cmp, collections::HashMap};

pub struct Solution {}

impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let mut res = 0;
        let mut i = 0;
        let mut j = 0;
        let strs: Vec<char> = s.chars().collect();
        let mut map: HashMap<char, i32> = HashMap::new();

        while j < strs.len() {
            map.entry(strs[j]).and_modify(|c| *c += 1).or_insert(1);
            let f_max = map.values().max().unwrap();
            let remains = (j - i + 1) as i32 - *f_max;
            if remains <= k {
                res = cmp::max(res, (j - i + 1) as i32);
                j += 1;
            } else {
                map.entry(strs[i]).and_modify(|c| *c -= 1).or_default();
                map.entry(strs[j]).and_modify(|c| *c -= 1).or_default();
                i += 1;
            }
        }

        return res;
    }

    pub fn character_replacement2(s: String, k: i32) -> i32 {
        let mut res = 0;
        let mut i = 0;
        let strs: Vec<char> = s.chars().collect();
        let mut map: HashMap<char, i32> = HashMap::new();

        for j in 0..s.len() {
            map.entry(strs[j]).and_modify(|c| *c += 1).or_insert(1);
            while (j - i + 1) as i32 - map.values().max().unwrap() > k {
                map.entry(strs[i]).and_modify(|c| *c -= 1).or_default();
                i += 1;
            }

            res = cmp::max(res, (j - i + 1) as i32);
        }

        return res;
    }

    pub fn tests() {
        let s = "ABAB".to_string();
        let k = 2;
        let expected = 4;
        let actual = Solution::character_replacement(s, k);

        assert_eq!(actual, expected);

        let s2 = "AABABBA".to_string();
        let k2 = 1;
        let expected2 = 4;
        let actual2 = Solution::character_replacement(s2, k2);

        assert_eq!(actual2, expected2);

        let s3 = "ABBB".to_string();
        let k3 = 2;
        let expected3 = 4;
        let actual3 = Solution::character_replacement(s3, k3);

        assert_eq!(actual3, expected3);

        let s = "ABAB".to_string();
        let k = 2;
        let expected = 4;
        let actual = Solution::character_replacement2(s, k);

        assert_eq!(actual, expected);

        let s2 = "AABABBA".to_string();
        let k2 = 1;
        let expected2 = 4;
        let actual2 = Solution::character_replacement2(s2, k2);

        assert_eq!(actual2, expected2);

        let s3 = "ABBB".to_string();
        let k3 = 2;
        let expected3 = 4;
        let actual3 = Solution::character_replacement2(s3, k3);

        assert_eq!(actual3, expected3);
    }
}
