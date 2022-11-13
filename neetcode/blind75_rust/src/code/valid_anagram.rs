use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut map: HashMap<char, i32> = HashMap::new();

        if s.len() != t.len() {
            return false;
        }

        s.chars().zip(t.chars()).for_each(|(s, t)| {
            if s == t {
                return;
            }

            map.entry(s)
                .and_modify(|counter| *counter += 1)
                .or_insert(1);
            map.entry(t)
                .and_modify(|counter| *counter -= 1)
                .or_insert(-1);
        });

        // NOTE: more complicated
        // let mut res = true;
        // map.values().for_each(|v| {
        //     if *v != 0 {
        //         res = false;
        //     }
        // });
        //
        // return res;

        return map.values().find(|&&x| x != 0).is_none();
    }

    pub fn tests() {
        let s = String::from("anagram");
        let t = String::from("nagaram");
        let res = Solution::is_anagram(s, t);
        assert_eq!(res, true);
    }
}
