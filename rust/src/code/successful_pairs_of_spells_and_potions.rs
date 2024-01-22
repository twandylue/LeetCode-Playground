struct Solution {}

impl Solution {
    // NOTE: time complexity: O(mlogm + nlogm)
    pub fn successful_pairs(spells: Vec<i32>, mut potions: Vec<i32>, success: i64) -> Vec<i32> {
        potions.sort();
        let mut result: Vec<i32> = Vec::new();
        let spells: Vec<i64> = spells.iter().map(|x| *x as i64).collect();
        let potions: Vec<i64> = potions.iter().map(|x| *x as i64).collect();
        for s in spells.iter() {
            let s: i64 = *s as i64;
            let target: i64 = if success % s > 0 {
                success / s + 1
            } else {
                success / s
            };
            let index: i32 = Self::find_most_lest_large_number(&potions, target);
            if index == -1 {
                result.push(0);
            } else {
                result.push(potions.len() as i32 - index);
            }
        }

        result
    }

    fn find_most_lest_large_number(potions: &Vec<i64>, target: i64) -> i32 {
        let mut result: i32 = -1;
        let mut l: usize = 0;
        let mut r: usize = potions.len() - 1;
        while l <= r {
            let mid: usize = (l + r) / 2;
            if potions[mid] == target {
                result = mid as i32;
                if mid.checked_sub(1).is_none() {
                    break;
                }
                r = mid - 1;
            } else if potions[mid] > target {
                result = mid as i32;
                if mid.checked_sub(1).is_none() {
                    break;
                }
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_successful_pairs_case_1() {
        // arrange
        let spells: Vec<i32> = vec![5, 1, 3];
        let potions: Vec<i32> = vec![1, 2, 3, 4, 5];
        let success: i64 = 7;
        let expected: Vec<i32> = vec![4, 0, 3];

        // act
        let actual = Solution::successful_pairs(spells, potions, success);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_successful_pairs_case_2() {
        // arrange
        let spells: Vec<i32> = vec![3, 1, 2];
        let potions: Vec<i32> = vec![8, 5, 8];
        let success: i64 = 16;
        let expected: Vec<i32> = vec![2, 0, 2];

        // act
        let actual = Solution::successful_pairs(spells, potions, success);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_successful_pairs_case_3() {
        // arrange
        let spells: Vec<i32> = vec![15, 8, 19];
        let potions: Vec<i32> = vec![38, 36, 23];
        let success: i64 = 328;
        let expected: Vec<i32> = vec![3, 0, 3];

        // act
        let actual = Solution::successful_pairs(spells, potions, success);

        // assert
        assert_eq!(expected, actual);
    }
}
