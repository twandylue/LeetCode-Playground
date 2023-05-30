use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        let mut min_intervals: (usize, usize) = (0, 0);
        let mut interval_len: usize = usize::MAX;
        let mut have = 0;
        let mut have_map: HashMap<char, i32> = HashMap::new();
        let mut need_map: HashMap<char, i32> = HashMap::new();
        for c in t.chars() {
            need_map.entry(c).and_modify(|v| *v += 1).or_insert(1);
        }
        let need = need_map.keys().len();
        let s_chars: Vec<char> = s.chars().collect();

        let mut l = 0;
        for r in 0..s_chars.len() {
            let c_r = s_chars[r];
            have_map
                .entry(c_r)
                .and_modify(|v| {
                    *v += 1;
                })
                .or_insert(1);

            match need_map.get(&c_r) {
                Some(&n_v) => {
                    if let Some(&h_v) = have_map.get(&c_r) {
                        if n_v == h_v {
                            have += 1;
                        }
                    }
                }
                None => (),
            }

            while have == need {
                Self::update_min_interval(&mut min_intervals, &mut interval_len, l, r);

                let c_l = s_chars[l];

                have_map.entry(c_l).and_modify(|v| *v -= 1);
                match need_map.get(&c_l) {
                    Some(&v_n) => {
                        if let Some(&v_h) = have_map.get(&c_l) {
                            if v_n == v_h + 1 {
                                have -= 1;
                            }
                        }
                    }
                    None => (),
                }
                l += 1;
            }
        }

        if interval_len == usize::MAX {
            return String::new();
        } else {
            return s[min_intervals.0..=min_intervals.1].to_string();
        }
    }

    fn update_min_interval(
        min_interval: &mut (usize, usize),
        min_interval_len: &mut usize,
        l: usize,
        r: usize,
    ) {
        if (r + 1 - l) < *min_interval_len {
            *min_interval = (l, r);
            *min_interval_len = r + 1 - l;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn minimum_window_substring_case_1() {
        // arrange
        let s = String::from("ADOBECODEBANC");
        let t = String::from("ABC");
        let expected = String::from("BANC");

        // act
        let actual = Solution::min_window(s, t);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn minimum_window_substring_case_2() {
        // arrange
        let s = String::from("a");
        let t = String::from("a");
        let expected = String::from("a");

        // act
        let actual = Solution::min_window(s, t);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn minimum_window_substring_case_3() {
        // arrange
        let s = String::from("a");
        let t = String::from("aa");
        let expected = String::from("");

        // act
        let actual = Solution::min_window(s, t);

        // assert
        assert_eq!(expected, actual);
    }
}
