struct Solution {}

impl Solution {
    pub fn num_unique_emails(emails: Vec<String>) -> i32 {
        use std::collections::HashSet;
        let mut email_set: HashSet<(String, String)> = HashSet::new();

        for email in emails.iter() {
            let s: Vec<&str> = email.split("@").collect();
            let local_name: &str = s[0];
            let domain_name: &str = s[1];
            let mut local_name: String = local_name.replace(".", "");
            if let Some(i) = local_name.find('+') {
                local_name = local_name.chars().collect::<Vec<char>>()[..i]
                    .iter()
                    .collect::<String>();
            }
            email_set.insert((domain_name.to_string(), local_name));
        }

        return email_set.len() as i32;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn num_unique_emails_case_1() {
        // arrange
        let emails: Vec<String> = vec![
            "test.email+alex@leetcode.com".to_string(),
            "test.e.mail+bob.cathy@leetcode.com".to_string(),
            "testemail+david@lee.tcode.com".to_string(),
        ];
        let expected: i32 = 2;

        // act
        let actual = Solution::num_unique_emails(emails);

        // assert
        assert_eq!(expected, actual)
    }
}
