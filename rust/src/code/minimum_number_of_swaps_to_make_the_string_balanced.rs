struct Solution {}

impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut curr_close_pre: i32 = 0;
        let mut max_close_pre: i32 = 0;

        for i in 0..s.len() {
            if s[i] == ']' {
                curr_close_pre += 1;
            } else {
                curr_close_pre -= 1;
            }

            max_close_pre = std::cmp::max(max_close_pre, curr_close_pre);
        }

        return ((max_close_pre + 1) as f32 / 2_f32) as i32;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn min_swaps_case_1() {
        // arrange
        let s: String = "][][".to_string();
        let expected: i32 = 1;

        // act
        let actual = Solution::min_swaps(s);

        // arrange
        assert_eq!(expected, actual);
    }
}
