use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        let tuples = [("]", "["), ("}", "{"), (")", "(")];
        let map: HashMap<&str, &str> = tuples.into_iter().collect();

        s.chars().for_each(|x| {
            // TODO:
            // if map.contains_key(x) {}
            stack.push(x);
        });

        return true;
    }

    pub fn tests() {
        let s = "()".to_string();
        let expected = true;

        let s2 = "()[]{}".to_string();
        let expected2 = true;

        let s3 = "(]".to_string();
        let expected3 = false;
    }
}
