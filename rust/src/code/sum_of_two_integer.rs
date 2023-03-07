pub struct Solution {}

impl Solution {
    pub fn get_sum(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let temp = (a & b) << 1;
            a ^= b;
            b = temp;
        }
        a
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let a = 1;
        let b = 2;
        let expected = 3;
        let actual = Solution::get_sum(a, b);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let a = 2;
        let b = 3;
        let expected = 5;
        let actual = Solution::get_sum(a, b);

        assert_eq!(expected, actual);
    }
}
