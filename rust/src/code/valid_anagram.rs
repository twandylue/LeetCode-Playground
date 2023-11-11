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

    pub fn is_anagram3(s: String, t: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();

        if t.len() != s.len() {
            return false;
        }
        let mut alph: [i32; 26] = [0; 26];
        for i in 0..s.len() {
            alph[(s[i] as u8 - 'a' as u8) as usize] += 1;
            alph[(t[i] as u8 - 'a' as u8) as usize] -= 1;
        }

        for i in 0..alph.len() {
            if alph[i] != 0 {
                return false;
            }
        }

        return true;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn is_anagram_case_1() {
        // arrange
        let s = String::from("anagram");
        let t = String::from("nagaram");

        // act
        let res = Solution::is_anagram(s.to_string(), t.to_string());

        // assert
        assert_eq!(res, true);
    }

    #[test]
    fn is_anagram_case_2() {
        // arrange
        let s = String::from("anagram");
        let t = String::from("nagaram");

        // act
        let res = Solution::is_anagram2(s.to_string(), t.to_string());

        // assert
        assert_eq!(res, true);
    }

    #[test]
    fn is_anagram_case_3() {
        // arrange
        let s = String::from("anagram");
        let t = String::from("nagaram");

        // act
        let res = Solution::is_anagram3(s.to_string(), t.to_string());

        // assert
        assert_eq!(res, true);
    }
}
