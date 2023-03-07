pub struct Solution {}

impl Solution {
    #[allow(non_snake_case)]
    pub fn hammingWeight(mut n: u32) -> i32 {
        let mut res: u32 = 0;
        while n > 0 {
            res += n % 2;
            n = n >> 1;
        }

        return res as i32;
    }

    #[allow(non_snake_case)]
    pub fn hammingWeight_2(mut n: u32) -> i32 {
        let mut res: u32 = 0;
        while n > 0 {
            n = n & (n - 1);
            res += 1;
        }

        return res as i32;
    }
}

#[cfg(test)]
pub mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let n = 0b00000000000000000000000000001011;
        let expected = 3;
        let actual = Solution::hammingWeight(n);
        let actual_2 = Solution::hammingWeight_2(n);
        assert_eq!(expected, actual);
        assert_eq!(expected, actual_2);
    }

    #[test]
    fn case_2() {
        let n = 0b00000000000000000000000010000000;
        let expected = 1;
        let actual = Solution::hammingWeight(n);
        let actual_2 = Solution::hammingWeight_2(n);
        assert_eq!(expected, actual);
        assert_eq!(expected, actual_2);
    }

    #[test]
    fn case_3() {
        let n = 0b11111111111111111111111111111101;
        let expected = 31;
        let actual = Solution::hammingWeight(n);
        let actual_2 = Solution::hammingWeight_2(n);
        assert_eq!(expected, actual);
        assert_eq!(expected, actual_2);
    }
}
