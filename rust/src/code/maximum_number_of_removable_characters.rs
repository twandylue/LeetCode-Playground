use std::collections::HashSet;

struct Solution {}

impl Solution {
    // TODO: over time limiting
    pub fn maximum_removals(s: String, p: String, removable: Vec<i32>) -> i32 {
        if removable.len() == 0 {
            return 0;
        }

        let s: Vec<char> = s.chars().collect();
        let p: Vec<char> = p.chars().collect();
        let mut result: i32 = 0;
        let mut l: usize = 0;
        let mut r: usize = removable.len() - 1;
        while l <= r {
            let mid: usize = (l + r) / 2;
            let removable_set: HashSet<i32> = removable[..mid + 1].iter().cloned().collect();
            if Self::is_subsequence(&s, &p, &removable_set) {
                result = mid as i32 + 1;
                l = mid + 1;
            } else {
                if mid.checked_sub(1).is_none() {
                    break;
                }
                r = mid - 1;
            }
        }

        result
    }

    fn is_subsequence(s: &Vec<char>, p: &Vec<char>, removable_set: &HashSet<i32>) -> bool {
        let mut i: usize = 0;
        let mut j: usize = 0;
        while i < s.len() {
            if removable_set.contains(&(i as i32)) || (j < p.len() && s[i] != p[j]) {
                i += 1;
                continue;
            }
            if j < p.len() && s[i] == p[j] {
                i += 1;
            }
            j += 1;
        }

        j == p.len()
    }
}
