struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        use std::cmp::max;

        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();
        let mut l: usize = 0;
        let mut result: i32 = 0;
        let mut curr_cost: i32 = 0;
        for r in 0..s.len() {
            curr_cost += ((s[r] as i8 - t[r] as i8) as i32).abs();
            while curr_cost > max_cost {
                curr_cost -= ((s[l] as i8 - t[l] as i8) as i32).abs();
                l += 1;
            }
            if l <= r {
                result = max(result, (r - l + 1) as i32);
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_equal_substring_case_1() {
        // arrange
        let s: String = "abcd".to_string();
        let t: String = "bcdf".to_string();
        let maxCost: i32 = 3;
        let expected: i32 = 3;

        // act
        let actual = Solution::equal_substring(s, t, maxCost);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_equal_substring_case_2() {
        // arrange
        let s: String = "abcd".to_string();
        let t: String = "cdef".to_string();
        let maxCost: i32 = 3;
        let expected: i32 = 1;

        // act
        let actual = Solution::equal_substring(s, t, maxCost);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_equal_substring_case_3() {
        // arrange
        let s: String = "abcd".to_string();
        let t: String = "acde".to_string();
        let maxCost: i32 = 0;
        let expected: i32 = 1;

        // act
        let actual = Solution::equal_substring(s, t, maxCost);

        // assert
        assert_eq!(expected, actual);
    }
}
