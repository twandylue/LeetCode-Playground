struct Solution {}

impl Solution {
    pub fn smallest_number(num: i64) -> i64 {
        if num == 0 {
            return 0;
        }

        let mut num_strs: Vec<char> = num.to_string().chars().collect();

        if num > 0 {
            num_strs.sort();
            let mut first_non_zero_index: usize = 0;
            for i in 0..num_strs.len() {
                if num_strs[i] != '0' {
                    first_non_zero_index = i;
                    break;
                }
            }
            let tmp: char = num_strs[first_non_zero_index];
            num_strs[first_non_zero_index] = '0';
            num_strs[0] = tmp;

            return num_strs.iter().collect::<String>().parse::<i64>().unwrap();
        }

        let mut number_parts: Vec<char> = num_strs[1..].to_vec();
        number_parts.sort_by(|a, b| b.cmp(a));
        return -1
            * number_parts
                .iter()
                .collect::<String>()
                .parse::<i64>()
                .unwrap();
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn smallest_number_case_1() {
        // arrange
        let num: i64 = 310;
        let expected: i64 = 103;

        // act
        let actual = Solution::smallest_number(num);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn smallest_number_case_2() {
        // arrange
        let num: i64 = -7605;
        let expected: i64 = -7650;

        // act
        let actual = Solution::smallest_number(num);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn smallest_number_case_3() {
        // arrange
        let num: i64 = 0;
        let expected: i64 = 0;

        // act
        let actual = Solution::smallest_number(num);

        // assert
        assert_eq!(expected, actual);
    }
}
