struct Solution {}

impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = 0;

        while r < chars.len() {
            let mut count: i32 = 1;
            while r < chars.len() - 1 && chars[r] == chars[r + 1] {
                count += 1;
                r += 1;
            }
            chars[l] = chars[r];
            l += 1;
            if count != 1 {
                for n in count.to_string().chars() {
                    if l < chars.len() {
                        chars[l] = n;
                        l += 1
                    } else {
                        break;
                    }
                }
            }
            r += 1;
        }

        l as i32
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
