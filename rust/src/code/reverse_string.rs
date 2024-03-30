struct Solution {}

impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut l: usize = 0;
        let mut r: usize = s.len() - 1;

        while l < r {
            let tmp: char = s[l];
            s[l] = s[r];
            s[r] = tmp;
            l += 1;
            r -= 1;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_string_case_1() {
        // arrange
        let mut s: Vec<char> = vec!['h', 'e', 'l', 'l', 'o'];
        let expected: Vec<char> = vec!['o', 'l', 'l', 'e', 'h'];
        // act
        Solution::reverse_string(&mut s);

        // assert
        assert_eq!(expected, s);
    }
}
