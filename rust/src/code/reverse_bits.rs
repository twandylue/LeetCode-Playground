pub struct Solution {}

impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut res = 0;
        for n in 0..=31 {
            let bit = (x >> n) & 1;
            res = bit << (31 - n) | res
        }

        res
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let n = 0b00000010100101000001111010011100;
        let expected = 964176192;
        let actual = Solution::reverse_bits(n);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let n = 0b11111111111111111111111111111101;
        let expected = 3221225471;
        let actual = Solution::reverse_bits(n);

        assert_eq!(expected, actual);
    }
}
