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

    // O(NlogN)
    pub fn is_anagram2(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut v_s: Vec<u32> = s.chars().map(|x| x as u32).collect();
        let mut v_t: Vec<u32> = t.chars().map(|x| x as u32).collect();
        v_s.sort_by(|a, b| a.cmp(b));
        v_t.sort_by(|a, b| a.cmp(b));

        return v_s.eq(&v_t);
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let s = String::from("anagram");
        let t = String::from("nagaram");
        let res = Solution::is_anagram(s.to_string(), t.to_string());
        let res2 = Solution::is_anagram2(s.clone(), t.clone());
        assert_eq!(res, true);
        assert_eq!(res2, true);
    }
}
