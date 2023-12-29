struct Solution {}

impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        if chars.len() == 1 {
            return 1;
        }

        let mut l: usize = 0;
        let mut r: usize = 1;
        let mut curr: usize = 0;
        while r < chars.len() {
            while r < chars.len() && chars[l] == chars[r] {
                r += 1;
            }

            chars[curr] = chars[l];
            curr += 1;
            let count: String = (r - l).to_string();
            if count == "1".to_string() {
                l = r;
                continue;
            }
            for c in count.chars() {
                chars[curr] = c;
                curr += 1
            }

            l = r;
        }

        curr as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_compress_case_1() {
        // arrange
        let mut chars: Vec<char> = vec!['a', 'a', 'b', 'b', 'c', 'c', 'c'];
        let expected: i32 = 6;

        // act
        let actual = Solution::compress(&mut chars);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_compress_case_2() {
        // arrange
        let mut chars: Vec<char> = vec!['a'];
        let expected: i32 = 1;

        // act
        let actual = Solution::compress(&mut chars);

        // assert
        assert_eq!(expected, actual);
    }
}
