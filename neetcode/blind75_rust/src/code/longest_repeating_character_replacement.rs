use std::cmp;

pub struct Solution {}

impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let mut res = 0;
        let mut i = 0;
        let mut j = 0;
        let strs: Vec<char> = s.chars().collect();
        let mut map = vec![0; 26];

        while j < strs.len() {
            let s_index = (strs[j] as u8 - 65) as usize;
            map[s_index] += 1;
            let f_max = map.iter().max().unwrap();
            let remains = (j - i + 1 - *f_max) as i32;
            if remains <= k {
                res = cmp::max(res, (j - i + 1) as i32);
                j += 1;
            } else {
                let e_index = (strs[i] as u8 - 65) as usize;
                map[s_index] -= 1;
                map[e_index] -= 1;
                i += 1;
            }
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
    }
}
