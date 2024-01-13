struct Solution {}

impl Solution {
    pub fn remove_kdigits(num: String, mut k: i32) -> String {
        let mut stack: Vec<u8> = Vec::new();
        let num: Vec<u8> = num.chars().map(|x| x as u8).collect();
        for i in 0..num.len() {
            while stack.len() > 0 && k > 0 && stack[stack.len() - 1] > num[i] {
                stack.pop().unwrap();
                k -= 1;
            }
            stack.push(num[i]);
        }

        while stack.len() > 0 && k > 0 {
            stack.pop().unwrap();
            k -= 1;
        }

        let stack: Vec<char> = stack.iter().map(|x| *x as char).collect();
        let mut p: usize = 0;
        for i in 0..stack.len() {
            if stack[i] == '0' {
                p += 1;
            } else if stack[i] != '0' {
                break;
            }
        }

        let result: String = stack[p..].iter().collect();
        return if result.len() == 0 {
            "0".to_string()
        } else {
            result
        };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_remove_kdigits_case_1() {
        // arrange
        let num: String = "1432219".to_string();
        let k: i32 = 3;
        let expected: String = "1219".to_string();

        // act
        let mut actual = Solution::remove_kdigits(num, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_remove_kdigits_case_2() {
        // arrange
        let num: String = "10200".to_string();
        let k: i32 = 1;
        let expected: String = "200".to_string();

        // act
        let mut actual = Solution::remove_kdigits(num, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_remove_kdigits_case_3() {
        // arrange
        let num: String = "10".to_string();
        let k: i32 = 2;
        let expected: String = "0".to_string();

        // act
        let mut actual = Solution::remove_kdigits(num, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_remove_kdigits_case_4() {
        // arrange
        let num: String = "9".to_string();
        let k: i32 = 1;
        let expected: String = "0".to_string();

        // act
        let mut actual = Solution::remove_kdigits(num, k);

        // assert
        assert_eq!(expected, actual);
    }
}
