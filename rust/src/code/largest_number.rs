use std::cmp::Ordering;

struct Solution {}

impl Solution {
    // NOTE: time complexity: O(nlogn)
    // Comparing two String and sorting
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut nums_strs: Vec<String> = vec!["".to_string(); nums.len()];
        for i in 0..nums.len() {
            nums_strs[i] = nums[i].to_string();
        }
        nums_strs.sort_by(|a, b| Self::compare(a, b));

        return if nums_strs[0] == "0".to_string() {
            "0".to_string()
        } else {
            nums_strs.join("")
        };
    }

    fn compare(n1: &str, n2: &str) -> Ordering {
        let num1: String = format!("{}{}", n1, n2);
        let num2: String = format!("{}{}", n2, n1);
        if let (Some(n1), Some(n2)) = (num1.parse::<i128>().ok(), num2.parse::<i128>().ok()) {
            if n1 > n2 {
                return Ordering::Less;
            } else {
                return Ordering::Greater;
            }
        } else {
            unreachable!("Something is wrong...")
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn largest_number_case_1() {
        // arrange
        let nums: Vec<i32> = vec![10, 2];
        let expected: String = "210".to_string();

        // act
        let actual = Solution::largest_number(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn largest_number_case_2() {
        // arrange
        let nums: Vec<i32> = vec![3, 34];
        let expected: String = "343".to_string();

        // act
        let actual = Solution::largest_number(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn largest_number_case_3() {
        // arrange
        let nums: Vec<i32> = vec![999999991, 9];
        let expected: String = "9999999991".to_string();

        // act
        let actual = Solution::largest_number(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn largest_number_case_4() {
        // arrange
        let nums: Vec<i32> = vec![1000000000, 1000000000];
        let expected: String = "10000000001000000000".to_string();

        // act
        let actual = Solution::largest_number(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
