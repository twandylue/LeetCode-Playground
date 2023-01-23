pub struct Solution {}

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let iter = s
            .chars()
            .filter(|c| c.is_alphanumeric())
            .map(|x| x.to_ascii_lowercase());

        return iter.clone().eq(iter.rev());
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let s = "A man, a plan, a canal: Panama".to_string();
        let expected = true;
        let actual = Solution::is_palindrome(s);
        assert_eq!(actual, expected);

        let s2 = "race a car".to_string();
        let expected2 = false;
        let actual2 = Solution::is_palindrome(s2);
        assert_eq!(actual2, expected2);

        let s3 = " ".to_string();
        let expected3 = true;
        let actual3 = Solution::is_palindrome(s3);
        assert_eq!(actual3, expected3);
    }
}
