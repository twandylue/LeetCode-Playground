use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        let map = HashMap::from([(']', '['), ('}', '{'), (')', '(')]);
        let target: Vec<char> = s.chars().collect();

        for i in 0..target.len() {
            if map.contains_key(&target[i]) {
                if stack.len() == 0 {
                    return false;
                } else {
                    let p = stack.pop().unwrap();
                    let a = map.get(&target[i]).unwrap();
                    if p != *a {
                        return false;
                    }
                }
            } else {
                stack.push(target[i]);
            }
        }

        if stack.len() != 0 {
            return false;
        }

        return true;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let s = "()".to_string();
        let expected = true;
        let actual = Solution::is_valid(s);

        assert_eq!(actual, expected);

        let s2 = "()[]{}".to_string();
        let expected2 = true;
        let actual2 = Solution::is_valid(s2);

        assert_eq!(actual2, expected2);

        let s3 = "(]".to_string();
        let expected3 = false;
        let actual3 = Solution::is_valid(s3);

        assert_eq!(actual3, expected3);
    }
}
