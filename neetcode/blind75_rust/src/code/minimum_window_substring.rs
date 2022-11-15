use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        let mut start = 0;
        let mut end = 0;
        let ret = String::new();
        let mut t_map: HashMap<char, i32> = HashMap::new();
        let mut record_map: HashMap<char, i32> = HashMap::new();
        for i in t.chars() {
            t_map.entry(i).and_modify(|x| *x += 1).or_insert(1);
        }
        let target: Vec<char> = s.chars().collect();

        while end < target.len() {
            if !t_map.contains_key(&target[end]) {
                end += 1;
            } else {
                if *t_map.get(&target[end]).unwrap() == 0 {
                    // TODO:
                    // while target[start] !=  {
                    //
                    //
                    // }
                } else {
                    t_map.entry(target[end]).and_modify(|count| *count -= 1);
                }
            }
        }

        return ret;
    }

    pub fn tests() {
        let s = String::from("ADOBECODEBANC");
        let t = String::from("ABC");
        let expected = String::from("BANC");

        let s2 = String::from("a");
        let t2 = String::from("a");
        let expected2 = String::from("a");

        let s3 = String::from("a");
        let t3 = String::from("aa");
        let expected3 = String::from("");
    }
}
