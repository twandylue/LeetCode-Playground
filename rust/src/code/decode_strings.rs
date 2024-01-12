struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n^2)
    pub fn decode_string(s: String) -> String {
        use std::collections::VecDeque;

        let mut stack: Vec<char> = Vec::new();
        let s: Vec<char> = s.chars().collect();
        for i in 0..s.len() {
            if s[i] != ']' {
                stack.push(s[i]);
            } else {
                let mut accu: VecDeque<char> = VecDeque::new();
                while stack.len() > 0 && stack[stack.len() - 1] != '[' {
                    accu.push_front(stack.pop().unwrap());
                }
                stack.pop().unwrap();
                let mut times: VecDeque<char> = VecDeque::new();
                while stack.len() > 0 && stack[stack.len() - 1].is_digit(10) {
                    times.push_front(stack.pop().unwrap());
                }
                let times: i32 = times.iter().collect::<String>().parse::<i32>().unwrap();
                let mut result: Vec<char> = Vec::new();
                for _ in 0..times {
                    result.append(&mut accu.clone().into_iter().collect::<Vec<char>>());
                }
                stack.append(&mut result);
            }
        }

        stack.iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn daily_decode_string_case_1() {
        // arrange
        let s: String = "2[abc]3[cd]ef".to_string();
        let expected: String = "abcabccdcdcdef".to_string();

        // act
        let actual = Solution::decode_string(s);

        assert_eq!(expected, actual);
    }

    #[test]
    fn daily_decode_string_case_2() {
        // arrange
        let s: String = "abc3[cd]xyz".to_string();
        let expected: String = "abccdcdcdxyz".to_string();

        // act
        let actual = Solution::decode_string(s);

        assert_eq!(expected, actual);
    }

    #[test]
    fn daily_decode_string_case_3() {
        // arrange
        let s: String = "100[leetcode]".to_string();
        let expected: String = "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode".to_string();

        // act
        let actual = Solution::decode_string(s);

        assert_eq!(expected, actual);
    }
}
